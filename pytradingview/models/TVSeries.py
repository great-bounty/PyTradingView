from typing import Any, Dict, Optional
import sys
import logging

from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SeriesPriceScale = str
ChartStyle = int
EntityId = str


class TVSeries(TVObject):
    """
    TradingView Series API implementation.
    Corresponds to the ISeriesApi interface in TypeScript.
    """

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def isUserEditEnabled(self) -> bool:
        """
        Returns true if a user is able to remove/change/hide the main series.
        
        :return: True if the user is able to edit the main series
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setUserEditEnabled(self, enabled: bool) -> None:
        """
        Enables or disables removing/changing/hiding the main series by the user.
        
        :param enabled: Whether to enable user editing
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enabled": enabled}
        )
        logger.info(f"setUserEditEnabled: {resp.result}")

    async def mergeUp(self) -> None:
        """
        Merges the main series up (if possible).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"mergeUp: {resp.result}")

    async def mergeDown(self) -> None:
        """
        Merges the main series down (if possible).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"mergeDown: {resp.result}")

    async def unmergeUp(self) -> None:
        """
        Unmerges the main series up (if possible).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"unmergeUp: {resp.result}")

    async def unmergeDown(self) -> None:
        """
        Unmerges the main series down (if possible).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"unmergeDown: {resp.result}")

    async def detachToRight(self) -> None:
        """
        Pins the main series to a new price axis at right.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"detachToRight: {resp.result}")

    async def detachToLeft(self) -> None:
        """
        Pins the main series to a new price axis at left.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"detachToLeft: {resp.result}")

    async def detachNoScale(self) -> None:
        """
        Makes the main series to be an overlay source.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"detachNoScale: {resp.result}")

    async def changePriceScale(self, newPriceScale: SeriesPriceScale) -> None:
        """
        Changes the price scale of the main series.
        
        :param newPriceScale: New price scale ("new-left" | "new-right" | "no-scale" | EntityId)
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"newPriceScale": newPriceScale},
        )
        logger.info(f"changePriceScale: {resp.result}")

    async def isVisible(self) -> bool:
        """
        Returns true if the main series is visible.
        
        :return: True if the main series is visible
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setVisible(self, visible: bool) -> None:
        """
        Shows/hides the main series.
        
        :param visible: Whether the series is visible
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"visible": visible}
        )
        logger.info(f"setVisible: {resp.result}")

    async def bringToFront(self) -> None:
        """
        Places main series on top of all other chart objects.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"bringToFront: {resp.result}")

    async def sendToBack(self) -> None:
        """
        Places main series behind all other chart objects.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"sendToBack: {resp.result}")

    async def entityId(self) -> EntityId:
        """
        Value that is returned when a study is created via API.
        
        :return: Entity ID
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def chartStyleProperties(self, chartStyle: ChartStyle) -> Dict[str, Any]:
        """
        Returns properties for a specific chart style.
        
        :param chartStyle: Chart style type
        :return: Chart style properties object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"chartStyle": chartStyle},
        )
        return resp.result

    async def setChartStyleProperties(
        self, chartStyle: ChartStyle, newPrefs: Dict[str, Any]
    ) -> None:
        """
        Sets properties for a specific chart style.
        
        :param chartStyle: Chart style type
        :param newPrefs: New property configuration (partial)
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"chartStyle": chartStyle, "newPrefs": newPrefs},
        )
        logger.info(f"setChartStyleProperties: {resp.result}")
