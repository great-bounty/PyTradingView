import inspect
import asyncio
from typing import Callable, Dict, List, Any, Set

class TVSubscribeManager:
    _instance = None
    _event_handlers: Dict[str, List[Callable]] = {}
    _async_event_handlers: Dict[str, List[Callable]] = {}
    _cleanup_tasks: Set[asyncio.Task] = set()

    @classmethod
    def get_instance(cls) -> 'TVSubscribeManager':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if TVSubscribeManager._instance is not None:
            raise RuntimeError("Use get_instance() to access TVSubscribeManager")
        self._event_handlers = {}
        self._async_event_handlers = {}
        self._cleanup_tasks = set()

    def subscribe(self, event_name: str, handler: Callable) -> None:
        if event_name not in self._event_handlers:
            self._event_handlers[event_name] = []
        self._event_handlers[event_name].append(handler)
        caller = inspect.currentframe().f_back
        print(f"Handler subscribed to {event_name} by {caller.f_code.co_name}")

    def subscribe_async(self, event_name: str, handler: Callable) -> None:
        if event_name not in self._async_event_handlers:
            self._async_event_handlers[event_name] = []
        self._async_event_handlers[event_name].append(handler)

    def publish(self, event_name: str, *args, **kwargs) -> None:
        if event_name in self._event_handlers:
            for handler in self._event_handlers[event_name][:]:
                try:
                    handler(*args, **kwargs)
                except Exception as e:
                    print(f"Error in sync handler for {event_name}: {str(e)}")

    async def publish_async(self, event_name: str, *args, **kwargs) -> None:
        if event_name in self._async_event_handlers:
            tasks = []
            for handler in self._async_event_handlers[event_name]:
                try:
                    task = asyncio.create_task(handler(*args, **kwargs))
                    self._cleanup_tasks.add(task)
                    task.add_done_callback(self._cleanup_tasks.discard)
                    tasks.append(task)
                except Exception as e:
                    print(f"Error scheduling async handler for {event_name}: {str(e)}")
            
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

    def unsubscribe(self, event_name: str, handler: Callable) -> None:
        if event_name in self._event_handlers:
            self._event_handlers[event_name] = [
                h for h in self._event_handlers[event_name] if h != handler
            ]
        
        if event_name in self._async_event_handlers:
            self._async_event_handlers[event_name] = [
                h for h in self._async_event_handlers[event_name] if h != handler
            ]

class TVSubscribePublisher:
    def __init__(self):
        self.event_manager = TVSubscribeManager.get_instance()
    
    def setSymbol(self, symbol: str) -> None:
        print(f"[{inspect.currentframe().f_code.co_name}] Symbol set to {symbol}")
        
        self.event_manager.publish('symbol_changed', symbol)
        
        asyncio.create_task(
            self.event_manager.publish_async('symbol_changed_async', symbol)
        )

class TVSubscribeListener:
    def __init__(self):
        self.event_manager = TVSubscribeManager.get_instance()
        self._setup_event_listeners()
    
    def _setup_event_listeners(self) -> None:
        self.event_manager.subscribe('symbol_changed', self._on_symbol_changed)
        
        self.event_manager.subscribe_async('symbol_changed_async', self._on_symbol_changed_async)
    
    def _on_symbol_changed(self, symbol: str) -> None:
        print(f"[{inspect.currentframe().f_code.co_name}] Received symbol: {symbol}")
    
    async def _on_symbol_changed_async(self, symbol: str) -> None:
        try:
            print(f"[{inspect.currentframe().f_code.co_name}] Async received symbol: {symbol}")
            await self._process_symbol_async(symbol)
        except Exception as e:
            print(f"Error in async handler: {str(e)}")
    
    async def _process_symbol_async(self, symbol: str) -> None:
        await asyncio.sleep(0.1)
    
    def dispose(self) -> None:
        self.event_manager.unsubscribe('symbol_changed', self._on_symbol_changed)
        self.event_manager.unsubscribe('symbol_changed_async', self._on_symbol_changed_async)