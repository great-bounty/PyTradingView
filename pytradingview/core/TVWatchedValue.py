from __future__ import annotations
import asyncio
from typing import Any, Callable, Optional, Union, TypeVar, Generic
from .TVObject import TVObject, CallBackParams
from .TVBridgeObject import TVMethodResponse
import sys
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')

class TVWatchedValue(TVObject, Generic[T]):
    
    def __init__(self, object_id: str):
        self.object_id: str = object_id
        self._value_changed_callback: CallBackParams = None
        self._current_value: Optional[T] = None
    
    async def value(self) -> T:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        self._current_value = resp.result
        return resp.result
    
    async def setValue(self, value: T, forceUpdate: bool = False) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, 
            kwargs={"value": value, "forceUpdate": forceUpdate}
        )
        logger.info(f"setValue: {resp.result}")
    
    async def subscribe(self, callback: CallBackParams) -> None:
        self._value_changed_callback = callback
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"subscribe: {resp.result}")
    
    async def unsubscribe(self) -> None:
        self._value_changed_callback = None
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"unsubscribe: {resp.result}")
    
    async def onValueChanged(self, value: T) -> None:
        logger.info(f"onValueChanged: {value}")
        self._current_value = value
        
        if self._value_changed_callback:
            await self.handleCallbackFunction(
                callback=self._value_changed_callback, 
                value=value
            )