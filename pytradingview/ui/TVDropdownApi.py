from __future__ import annotations
from typing import Any, Dict, Optional
from ..core.TVObject import TVObject
from ..core.TVBridgeObject import TVMethodResponse
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TVDropdownApi(TVObject):
    """
    TradingView Dropdown API proxy class.
    Encapsulates dropdown menu operations.
    """

    def __init__(self, object_id: str):
        super().__init__(object_id)

    async def applyOptions(self, options: Dict[str, Any]) -> None:
        """
        Apply options to the dropdown menu.
        Note: This method does not affect the menu alignment. To change alignment, you need to remove and recreate the menu.
        
        @param options Partial options for the dropdown menu.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        logger.info(f"applyOptions: {resp.result}")

    async def remove(self) -> None:
        """
        Remove the dropdown menu.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"remove: {resp.result}")