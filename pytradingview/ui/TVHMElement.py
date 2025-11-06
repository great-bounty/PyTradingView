from typing import Any, Callable, Optional
from ..core.TVObject import TVObject, CallBackParams
from typing import Any, Callable, Dict, List, Optional, Union, AsyncGenerator, Awaitable
from ..core.TVBridgeObject import TVMethodResponse
import sys
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TVHMElement(TVObject):
    
    async def setTextContent(self, textContent: str) -> None:
        kwargs: dict[str, str] = {"textContent":textContent}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setTextContent: {resp.result}")

    async def setTitle(self, title: str):
        kwargs: dict[str, str] = {"title":title}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setTitle: {resp.result}")

    async def setAlign(self, align: str) -> None:
        kwargs: dict[str, str] = {"align":align}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setAlign: {resp.result}")
    
    async def onClick(self, callback: CallBackParams = None):
        self.onClick_callback: CallBackParams = callback
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"onClick: {resp.result}")
        
    async def onClickCallback(self) -> None:
        logger.info(f"onClickCallback successful")
        if self.onClick_callback:
            await self.handleCallbackFunction(callback=self.onClick_callback)

    async def setAttribute(self, qualifiedName: str, value: str) -> None:
        kwargs: dict[str, str] = {"qualifiedName":qualifiedName, "value":value}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setAttribute: {resp.result}")