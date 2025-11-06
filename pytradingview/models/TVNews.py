import sys
import logging

from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TVNews(TVObject):

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def refresh(self) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"refresh: {resp.result}")
