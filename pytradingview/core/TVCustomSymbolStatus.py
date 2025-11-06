from typing import Any
import sys
import logging

from .TVBridgeObject import TVMethodResponse
from .TVObject import TVObject
from .TVCustomSymbolStatusAdapter import TVCustomSymbolStatusAdapter


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




class TVCustomSymbolStatus(TVObject):

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def symbol(self, symbolId: str) -> TVCustomSymbolStatusAdapter:

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"symbolId": symbolId}
        )
        return TVCustomSymbolStatusAdapter.get_or_create(object_id=resp.result)

    async def hideAll(self) -> None:

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"hideAll: {resp.result}")
