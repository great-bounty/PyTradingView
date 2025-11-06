from __future__ import annotations
import asyncio
from typing import Any, Awaitable, Callable, Optional, TypeVar, Generic, List
from .TVObject import TVObject, CallBackParams
from .TVBridgeObject import TVMethodResponse
import sys
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')

class TVSubscription(TVObject, Generic[T]):
    
    def __init__(self, object_id: str):
        super().__init__(object_id)
        self._event_callback: CallBackParams = None
        self._is_subscribed: bool = False
    
    async def subscribe(self, callback: CallBackParams, singleshot: bool = False) -> None:
        if self._is_subscribed:
            logger.warning("Already subscribed")
            return
        
        self._event_callback = callback
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, 
            kwargs={"singleshot": singleshot}
        )
        
        self._is_subscribed = True
        logger.info(f"subscribe: {resp.result}")
    
    async def unsubscribe(self) -> None:
        if not self._is_subscribed:
            logger.warning("Not subscribed")
            return
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        
        self._event_callback = None
        self._is_subscribed = False
        logger.info(f"unsubscribe: {resp.result}")
    
    async def unsubscribeAll(self) -> None:
        if not self._is_subscribed:
            logger.warning("Not subscribed")
            return
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        
        self._event_callback = None
        self._is_subscribed = False
        logger.info(f"unsubscribeAll: {resp.result}")
    
    async def onEventFired(self, args: List[Any]) -> None:
        logger.info(f"onEventFired: {args}")
        if len(args) == 1:
            arg0 = args[0]
            if isinstance(arg0, dict):
                params: dict = arg0
                if self._event_callback:
                    await self.handleCallbackFunction(
                        self._event_callback,
                        **params
                    )
            else:
                if self._event_callback:
                    await self.handleCallbackFunction(
                        self._event_callback,
                        arg0
                    )
        else:
            if self._event_callback:
                await self.handleCallbackFunction(
                    self._event_callback,
                    *args
                )