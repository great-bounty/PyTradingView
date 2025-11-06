from typing import Any, Dict, List, Optional, Union
import sys
import logging

from .TVBridgeObject import TVMethodResponse
from .TVObject import TVObject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


CustomStatusDropDownContent = Dict[str, Any]


class TVCustomSymbolStatusAdapter(TVObject):

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def getVisible(self) -> bool:
 
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setVisible(self, visible: bool) -> "TVCustomSymbolStatusAdapter":

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"visible": visible}
        )
        logger.info(f"setVisible: {resp.result}")
        return self

    async def getIcon(self) -> Optional[str]:

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setIcon(self, icon: Optional[str]) -> "TVCustomSymbolStatusAdapter":

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"icon": icon}
        )
        logger.info(f"setIcon: {resp.result}")
        return self

    async def getColor(self) -> str:

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setColor(self, color: str) -> "TVCustomSymbolStatusAdapter":

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"color": color}
        )
        logger.info(f"setColor: {resp.result}")
        return self

    async def getTooltip(self) -> Optional[str]:

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTooltip(self, tooltip: Optional[str]) -> "TVCustomSymbolStatusAdapter":
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"tooltip": tooltip}
        )
        logger.info(f"setTooltip: {resp.result}")
        return self

    async def getDropDownContent(self) -> Optional[List[CustomStatusDropDownContent]]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setDropDownContent(
        self, content: Optional[List[CustomStatusDropDownContent]]
    ) -> "TVCustomSymbolStatusAdapter":
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"content": content}
        )
        logger.info(f"setDropDownContent: {resp.result}")
        return self
