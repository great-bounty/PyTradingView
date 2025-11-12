import socket
import threading
import asyncio
import logging
from threading import Event
from typing import Dict, Any, Optional, TYPE_CHECKING, Callable, Awaitable
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import aiohttp
from pathlib import Path
from .TVBridgeObject import TVMethodCall, TVMethodResponse
from .TVObject import TVObject

if TYPE_CHECKING:
    from .TVWidgetConfig import TVWidgetConfig
    from .TVWidget import TVWidget


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TVBridge(object):
    
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.node_server_port = 6002
        self.is_connected_to_node = False
        
        self.bridge_port = 6100
        self.bridge_http_app = FastAPI()
        self.start_event = Event()
        
        # TVEngine 集成
        self._config_provider: Optional['TVWidgetConfig'] = None
        self._chart_ready_callback: Optional[Callable[['TVWidget'], Awaitable[None]]] = None
        
        self.bridge_http_app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        self.setup_routes()

    def register_config_provider(self, config: 'TVWidgetConfig') -> None:
        """
        注册配置提供者（由 TVEngine 调用）
        
        Args:
            config: TVWidgetConfig 实例
        """
        self._config_provider = config
        logger.info(f"Config provider registered: {config}")
    
    def register_chart_ready_callback(self, callback: Callable[['TVWidget'], Awaitable[None]]) -> None:
        """
        Register chart ready callback (called by TVEngine)
        
        This callback will be invoked when chart data is ready, triggering:
        - Chart initialization
        - Indicator activation
        - Initial indicator calculation on loaded data
        
        Args:
            callback: Async callback function to execute when chart is ready
        """
        self._chart_ready_callback = callback
        logger.info("Chart ready callback registered")
    
    def setup_routes(self):
        self._register_connection_routes()
        self._register_rpc_routes()

    def _register_connection_routes(self):
        @self.bridge_http_app.post("/ping")
        async def ping():
            return { 'ping': 'PY HTTP server running' }

        @self.bridge_http_app.post("/connect/from/nd")
        async def connect_from_nd():
            return {"bridge_port": self.bridge_port}
        
        @self.bridge_http_app.post("/ping/from/nd")
        async def ping_from_nd():
            return {"bridge_port": self.bridge_port}

    def _register_rpc_routes(self):
        @self.bridge_http_app.post("/web/call/py")
        async def web_call_py(data: dict):
            return await self._handle_web_to_python_call(data)

    async def _handle_web_to_python_call(self, data: Dict[str, Any]) -> TVMethodResponse:
        logger.info(f"Received RPC call: {data}")
        call_params = TVMethodCall.from_dict(data)
        
        # 分发到具体处理器
        if call_params.class_name == "TVWidget":
            resp = await self._handle_widget_call(call_params)
        elif call_params.class_name == "TVObjectPool":
            resp = await self._handle_object_pool_call(call_params)
        elif call_params.class_name == "TVBridge":
            resp = await self._handle_bridge_call(call_params)
        else:
            resp = await self._handle_generic_object_call(call_params)
        
        return TVMethodResponse.from_dict(resp)

    async def _handle_widget_call(self, params: TVMethodCall) -> dict:
        """
        处理 TVWidget 相关的 RPC 调用
        
        支持的方法：
        - widgetInitConfig: 返回 Widget 配置
        - chartDataReady: 触发图表就绪回调
        """
        WIDGET_CLASS_METHODS = {"widgetInitConfig", "chartDataReady"}
        
        if params.method_name  in WIDGET_CLASS_METHODS:
            if params.method_name == "widgetInitConfig":
                # 使用注册的配置提供者
                if self._config_provider:
                    result = self._config_provider.to_dict()
                else:
                    logger.warning("No config provider registered, returning None")
                    result = None
                return {"result": result}
            elif params.method_name == "chartDataReady":
                asyncio.create_task(self._handle_chart_data_ready(params))
                return {"result": "success"}
            else:
                return {"error": f"Invalid TVWidget method: {params.method_name}"}
        else:
            resp = await self._handle_generic_object_call(params)
            return resp

    async def _handle_object_pool_call(self, params: TVMethodCall) -> dict:
        from .TVObjectPool import TVObjectPool
        return TVObjectPool.get_instance().handle_remote_call(params)
    
    async def _handle_bridge_call(self, params: TVMethodCall) -> dict:
        if params.method_name == "runEnv":
            envPath = self._get_python_executable()
            filePath = str(Path(__file__).resolve())
            envInfos = {}
            if 'py_modules' in envPath or 'py_modules' in filePath:
                envInfos["env"] = "prod"
            else:
                envInfos["env"] = "dev"
            return {"result": envInfos}
        else:
            return {"error": f"Invalid TVBridge method: {params.method_name}"}
        
    async def _handle_generic_object_call(self, params: TVMethodCall) -> dict:
        error = self._validate_method_call(params)
        if error:
            return {"error": error}
        
        tv_obj = TVObject.get_instance(params.class_name, params.object_id)  # type: ignore
        return await tv_obj.handle_remote_call(params)

    def _validate_method_call(self, params: TVMethodCall) -> Optional[str]:
        if not params.class_name or not params.object_id or not params.method_name:
            error_msg = f"Invalid callParams: class_name={params.class_name}, object_id={params.object_id}, method_name={params.method_name}"
            logger.error(error_msg)
            return error_msg
        return None

    async def _handle_chart_data_ready(self, call_params: TVMethodCall):
        """
        Handle chart data ready event
        
        This method is triggered when TradingView chart completes initialization
        and chart data has been successfully loaded. At this point, K-line data
        is ready and we can safely perform indicator calculations.
        
        Flow:
        1. Retrieve TVWidget instance from object_id
        2. Invoke registered chart_ready_callback (set by TVEngine)
        3. The callback will initialize all charts and trigger indicator calculations
        
        Note: This is a critical entry point that bridges TradingView's JavaScript
        environment with Python indicator engine.
        
        Args:
            call_params: RPC call parameters containing widget object_id
        """
        try:
            from .TVWidget import TVWidget
            
            if not call_params.object_id:
                logger.error("_handle_chart_data_ready: object_id is None")
                return
            
            tvWidget: TVWidget = TVWidget.get_or_create(object_id=call_params.object_id)  # type: ignore
            
            if self._chart_ready_callback:
                await self._chart_ready_callback(tvWidget)
            else:
                logger.warning("No chart ready callback registered")
                
        except Exception as e:
            logger.exception(f"Error in _handle_chart_data_ready: {e}")
            
    def _is_port_available(self, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return True
            except OSError:
                return False
    
    def _find_available_port(self, start_port: int, max_attempts: int = 100) -> int:
        for offset in range(max_attempts):
            port = start_port + offset
            if self._is_port_available(port):
                return port
        raise RuntimeError(f"No available port found in range {start_port}-{start_port+max_attempts}")
    
    def _get_python_executable(self) -> str:
        # 返回规范化后的绝对路径（处理符号链接）
        return str(Path(sys.executable).resolve())
    
    async def start_connect_to_node_server(self):
        await self.connect_to_node_server()

    def start_http_server(self, on_port: int):
        if on_port > 0:
            self.bridge_port = on_port
        else:
            # 查找可用端口
            self.bridge_port = self._find_available_port(self.bridge_port)

        try:
            logger.info(f"Starting HTTP bridge server on 127.0.0.1:{self.bridge_port}")
            config = uvicorn.Config(
                self.bridge_http_app,
                host="127.0.0.1",
                port=self.bridge_port,
                log_level="info"
            )
            server = uvicorn.Server(config)
            
            original_startup = server.startup
            async def custom_startup(sockets=None):
                await original_startup(sockets=sockets)
                self.start_event.set()
                await self.start_connect_to_node_server()
            server.startup = custom_startup
            
            server.run()
        except Exception as e:
            logger.error(f"HTTP bridge server crashed: {str(e)}")
        else:
            pass

    def is_listening(self) -> bool:
        return self.start_event.is_set()
    
    async def connect_to_node_server(self, max_retries: int = 50, base_delay: float = 0.1) -> bool:
        original_port = self.node_server_port
        
        for retry in range(max_retries):
            if self.node_server_port >= 6100:
                break
                
            try:
                resp = await self._call_node_http_request(
                    "connect/from/py",
                    method='POST',
                    json_data={'bridge_port': self.bridge_port},
                    timeout=1
                )
                
                if resp and resp.get('nd_http_port'):
                    self.is_connected_to_node = True
                    self.node_server_port = resp['nd_http_port']
                    logger.info(f"Connected to Node server on port {self.node_server_port}")
                    return True
                    
            except Exception as e:
                logger.debug(f"Connection attempt {retry+1} failed on port {self.node_server_port}: {e}")
            
            if not self.is_connected_to_node:
                delay = min(base_delay * (2 ** min(retry, 5)), 5.0)
                await asyncio.sleep(delay)
                self.node_server_port = (self.node_server_port + 1) % 65536
        
        if not self.is_connected_to_node:
            logger.error(f"Failed to connect after {max_retries} attempts")
            self.node_server_port = original_port
        
        return self.is_connected_to_node

    async def call_node_server(self, params: TVMethodCall) -> TVMethodResponse:
        try:
            resp_json = await self._call_node_http_request(
                "py/call/web",
                method='POST',
                json_data=params.to_json()
            )
            if not resp_json:
                return TVMethodResponse(error="No response from Node server")
            return TVMethodResponse.from_dict(resp_json)
        except Exception as e:
            error_msg = f"Error calling {params.class_name}.{params.method_name}: {e}"
            logger.exception(error_msg)
            return TVMethodResponse(error=error_msg)

    async def _call_node_http_request(self, url: str, method: str = 'POST', 
                                       json_data: Optional[dict] = None, 
                                       timeout: int = 5) -> Optional[dict]:
        nd_url = f"http://127.0.0.1:{self.node_server_port}/{url}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(
                    method,
                    nd_url,
                    json=json_data,
                    timeout=aiohttp.ClientTimeout(total=timeout)
                ) as response:
                    response.raise_for_status()
                    return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            logger.debug(f"HTTP request to {nd_url} failed: {e}")
            return None
        except Exception as e:
            logger.exception(f"Unexpected error during HTTP request to {nd_url}")
            raise

    def run(self, on_port: int = 0):
        self.start_http_server(on_port=on_port)
