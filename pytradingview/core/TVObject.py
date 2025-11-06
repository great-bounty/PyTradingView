
from typing import Any, Literal, Callable, Dict, List, TypeAlias, TypeVar, Type, Optional, Union, AsyncGenerator, Awaitable
import asyncio
import json
import inspect
import logging
from .TVBridgeObject import TVMethodCall, TVMethodResponse
from .TVObjectPool import TVObjectPool

logger = logging.getLogger(__name__)

T = TypeVar('T', bound='TVObject')
CallBackParams: TypeAlias = Optional[Union[Callable[..., Any], Callable[..., Awaitable[Any]]]]

_CLASS_MAP_CACHE: Optional[Dict[str, Any]] = None


def get_class_map() -> Dict[str, Any]:
    global _CLASS_MAP_CACHE
    
    if _CLASS_MAP_CACHE is not None:
        return _CLASS_MAP_CACHE
    
    from .TVWidget import TVWidget
    from .TVChart import TVChart
    from ..ui.TVHMElement import TVHMElement
    from ..ui.TVContextMenuItem import TVContextMenuItem
    from ..trading.TVExecutionLine import TVExecutionLine
    from ..trading.TVOrderLine import TVOrderLine
    from ..trading.TVPositionLine import TVPositionLine
    from ..shapes.TVShape import TVShape
    from ..shapes.TVShapesGroupController import TVShapesGroupController
    from ..models.TVStudy import TVStudy
    from ..models.TVTimeScale import TVTimeScale
    from ..models.TVTimezone import TVTimezone
    from .TVWatchedValue import TVWatchedValue
    from .TVSubscription import TVSubscription
    from ..ui.TVDropdownApi import TVDropdownApi
    from ..models.TVPane import TVPane
    from ..models.TVSeries import TVSeries
    from ..shapes.TVSelection import TVSelection
    from .TVCustomSymbolStatus import TVCustomSymbolStatus
    from .TVCustomSymbolStatusAdapter import TVCustomSymbolStatusAdapter
    from .TVCustomThemes import TVCustomThemes
    from ..models.TVNews import TVNews
    from ..ui.TVWidgetbar import TVWidgetbar
    
    _CLASS_MAP_CACHE = {
        "TVWidget": TVWidget,
        "TVChart": TVChart,
        "TVHMElement": TVHMElement,
        "TVContextMenuItem": TVContextMenuItem,
        "TVExecutionLine": TVExecutionLine,
        "TVOrderLine": TVOrderLine,
        "TVPositionLine": TVPositionLine,
        "TVShape": TVShape,
        "TVShapesGroupController": TVShapesGroupController,
        "TVStudy": TVStudy,
        "TVTimeScale": TVTimeScale,
        "TVTimezone": TVTimezone,
        "TVWatchedValue": TVWatchedValue,
        "TVSubscription": TVSubscription,
        "TVDropdownApi": TVDropdownApi,
        "TVPane": TVPane,
        "TVSeries": TVSeries,
        "TVSelection": TVSelection,
        "TVCustomSymbolStatus": TVCustomSymbolStatus,
        "TVCustomSymbolStatusAdapter": TVCustomSymbolStatusAdapter,
        "TVCustomThemes": TVCustomThemes,
        "TVNews": TVNews,
        "TVWidgetbar": TVWidgetbar
    }
    
    logger.debug(f"Initialized class map with {len(_CLASS_MAP_CACHE)} classes")
    return _CLASS_MAP_CACHE

class TVObject:

    @classmethod
    def get_instance(cls, class_name: str, object_id: str) -> "TVObject":
        target_class = get_class_map().get(class_name)
        if target_class is None:
            raise TypeError(f"Unknown class name: '{class_name}'")
        
        instance = target_class.get_or_create(object_id=object_id)
        
        if not isinstance(instance, target_class):
            raise TypeError(
                f"Type mismatch for object '{object_id}': "
                f"expected {target_class.__name__}, got {type(instance).__name__}"
            )
        
        return instance

    @classmethod
    def get_or_create(cls: Type[T], object_id: str) -> T:
        if not isinstance(object_id, str):
            raise TypeError(
                f"object_id must be str, got {type(object_id).__name__}"
            )
        
        if not object_id.strip():
            raise ValueError(f"{cls.__name__}: object_id cannot be empty")

        pool = TVObjectPool.get_instance()
        existing_obj = pool.get_object_with_id(object_id)
        
        if existing_obj is not None:
            if not isinstance(existing_obj, cls):
                raise TypeError(
                    f"Object ID '{object_id}' already occupied by "
                    f"{type(existing_obj).__name__}, cannot use for {cls.__name__}"
                )
            logger.debug(f"Reusing existing {cls.__name__} with ID: {object_id}")
            return existing_obj  # type: ignore
        
        new_obj = cls(object_id)
        pool.register_object_with_id(new_obj, object_id)
        logger.debug(f"Created new {cls.__name__} with ID: {object_id}")
        return new_obj  # type: ignore

    def __init__(self, object_id: str):
        self.object_id = object_id

    async def invoke_callback(
        self, 
        callback: CallBackParams, 
        *args, 
        **kwargs
    ) -> Optional[Any]:
        if callback is None:
            return None
        
        try:
            if asyncio.iscoroutinefunction(callback):
                return await callback(*args, **kwargs)
            else:
                return callback(*args, **kwargs)  # type: ignore
        except Exception as e:
            logger.exception(f"Error invoking callback: {e}")
            raise
    
    async def handleCallbackFunction(
        self, 
        callback: CallBackParams, 
        *args, 
        **kwargs
    ) -> Optional[Any]:
        return await self.invoke_callback(callback, *args, **kwargs)

    def dispose(self):
        logger.debug(f"Disposing {self.__class__.__name__} with ID: {self.object_id}")
        TVObjectPool.get_instance().release(self.object_id)

    async def call_web_object_method(
        self, 
        method_name: str, 
        kwargs: Optional[Dict[str, Any]] = None
    ) -> TVMethodResponse:
        from .TVBridge import TVBridge
        
        call_params = TVMethodCall(
            class_name=self.__class__.__name__,
            object_id=self.object_id,
            method_name=method_name,
            kwargs=kwargs,
        )
        
        logger.debug(f"Calling remote method: {self.__class__.__name__}.{method_name}")
        response = await TVBridge.get_instance().call_node_server(call_params)
        
        if not response.is_success:
            logger.error(f"Remote call failed: {response.error} callParams: {call_params.to_json()}")
        
        return response
    
    async def handle_remote_call(self, call_params: TVMethodCall) -> dict:
        logger.info(
            f"{self.__class__.__name__}.{call_params.method_name} "
            f"called remotely (object_id={self.object_id})"
        )
        
        try:
            method = self._get_method(call_params.method_name)
            result = await self._invoke_method(method, call_params.kwargs or {})
            response = self._build_success_response(result)
            logger.debug(f"Remote call succeeded: {call_params.method_name}")
            return response
        except AttributeError:
            return self._build_method_not_found_error(call_params.method_name)
        except Exception as e:
            return self._build_error_response(
                call_params.method_name, 
                call_params.kwargs, 
                e
            )

    def _get_method(self, method_name: str) -> Callable:
        method = getattr(self, method_name, None)
        if not method or not callable(method):
            raise AttributeError(
                f"Method '{method_name}' not found in {self.__class__.__name__}"
            )
        return method

    async def _invoke_method(
        self, 
        method: Callable, 
        kwargs: Dict[str, Any]
    ) -> Any:
        if inspect.iscoroutinefunction(method):
            return await method(**kwargs)
        else:
            return method(**kwargs)

    def _build_success_response(self, result: Any) -> dict:
        if isinstance(result, TVObject) and result.object_id:
            return {'result': result.object_id}
        
        try:
            serializable_result = self._make_json_safe(result)
            json.dumps(serializable_result)
            return {'result': serializable_result}
        except TypeError as e:
            logger.warning(
                f"Result not JSON serializable for {type(result).__name__}: {e}, "
                f"converting to string"
            )
            return {'result': str(result)}

    def _make_json_safe(self, value: Any) -> Any:
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        
        if isinstance(value, dict):
            return {
                k: self._make_json_safe(v) 
                for k, v in value.items() 
                if self._should_include_attribute(k, v)
            }
        
        if isinstance(value, (list, tuple, set)):
            return [self._make_json_safe(item) for item in value]
        
        if hasattr(value, '__dict__'):
            return {
                k: self._make_json_safe(v) 
                for k, v in value.__dict__.items() 
                if self._should_include_attribute(k, v)
            }
        
        return value

    @staticmethod
    def _should_include_attribute(key: Any, value: Any) -> bool:
        if isinstance(key, str) and key.startswith('_'):
            return False
        if callable(value):
            return False
        return True

    def _build_method_not_found_error(self, method_name: str) -> dict:
        error_msg = (
            f"Method '{method_name}' not found or not callable "
            f"in {self.__class__.__name__}"
        )
        logger.error(error_msg)
        return {'error': error_msg}

    def _build_error_response(
        self, 
        method_name: str, 
        kwargs: Optional[Dict[str, Any]], 
        error: Exception
    ) -> dict:
        try:
            args_str = json.dumps(kwargs, ensure_ascii=False, indent=2)
        except (TypeError, ValueError):
            args_str = f"<non-serializable: {type(kwargs).__name__}>"
        
        error_msg = (
            f"Error calling {self.__class__.__name__}.{method_name} "
            f"with args: {args_str}. "
            f"{type(error).__name__}: {str(error)}"
        )
        
        logger.exception(error_msg)
        
        return {
            'error': f"{type(error).__name__}: {str(error)}",
            'method': method_name,
            'class': self.__class__.__name__
        }
