from typing import Any, List, Optional
import sys
import logging

from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TVPane(TVObject):
    """
    TradingView Pane API implementation.
    Corresponds to the IPaneApi interface in TypeScript.
    """

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def hasMainSeries(self) -> bool:
        """
        Returns true if the price scale contains the main series.
        
        :return: True if the price scale contains the main series
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getLeftPriceScales(self) -> List[Any]:
        """
        Returns an array of the PriceScaleApi instances that allows interaction with left price scales.
        The array may be empty if there is not any price scale on the left side of the pane.
        
        :return: Array of PriceScaleApi instances
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getRightPriceScales(self) -> List[Any]:
        """
        Returns an array of the PriceScaleApi instances that allows interaction with right price scales.
        The array may be empty if there is not any price scale on the right side of the pane.
        
        :return: Array of PriceScaleApi instances
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getMainSourcePriceScale(self) -> Optional[Any]:
        """
        Returns an instance of the PriceScaleApi that allows you to interact with the price scale of the main source
        or None if the main source is not attached to any price scale (it is in 'No Scale' mode).
        
        :return: PriceScaleApi instance or None
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getPriceScaleById(self, priceScaleId: str) -> Optional[Any]:
        """
        Returns an instance of the PriceScaleApi by price scale ID
        or None if the price scale cannot be found.
        
        :param priceScaleId: Price scale ID
        :return: PriceScaleApi instance or None
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"priceScaleId": priceScaleId},
        )
        return resp.result

    async def getHeight(self) -> int:
        """
        Returns the pane's height.
        
        :return: Pane height in pixels
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setHeight(self, height: int) -> None:
        """
        Sets the pane's height.
        
        :param height: Pane height in pixels
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"height": height}
        )
        logger.info(f"setHeight: {resp.result}")

    async def moveTo(self, paneIndex: int) -> None:
        """
        Moves the pane to a new position.
        paneIndex should be a number between 0 and all panes count - 1.
        
        :param paneIndex: Pane index, should be a number between 0 and all panes count - 1
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"paneIndex": paneIndex}
        )
        logger.info(f"moveTo: {resp.result}")

    async def paneIndex(self) -> int:
        """
        Returns the pane's index.
        It's a number between 0 and all panes count - 1.
        
        :return: Pane index, a number between 0 and all panes count - 1
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def collapse(self) -> None:
        """
        Collapse the current pane.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"collapse: {resp.result}")

    async def restore(self) -> None:
        """
        Restore the size of a previously collapsed pane.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"restore: {resp.result}")
