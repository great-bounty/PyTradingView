from typing import Any
import sys
import logging

from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PageName = str

class TVWidgetbar(TVObject):
    """
    TradingView Widgetbar API implementation.
    Corresponds to the IWidgetbarApi interface in TypeScript.
    """

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def showPage(self, pageName: PageName) -> None:
        """
        Show page.
        
        :param pageName: Name of page to show
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"pageName": pageName}
        )
        logger.info(f"showPage: {resp.result}")

    async def hidePage(self, pageName: PageName) -> None:
        """
        Hide page.
        
        :param pageName: Name of page to hide
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"pageName": pageName}
        )
        logger.info(f"hidePage: {resp.result}")

    async def isPageVisible(self, pageName: PageName) -> bool:
        """
        Checks if page is visible.
        
        :param pageName: Page to check if visible
        :return: True when page is visible
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"pageName": pageName}
        )
        return resp.result

    async def openOrderPanel(self) -> None:
        """
        Open order panel widget.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"openOrderPanel: {resp.result}")

    async def closeOrderPanel(self) -> None:
        """
        Close order panel widget.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"closeOrderPanel: {resp.result}")

    async def changeWidgetBarVisibility(self, visible: bool) -> None:
        """
        Change the visibility of the right toolbar.
        
        :param visible: True to display the toolbar, False to hide
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"visible": visible}
        )
        logger.info(f"changeWidgetBarVisibility: {resp.result}")

    async def destroy(self) -> None:
        """
        Cleans up (destroys) any subscriptions, intervals, or other resources owned by this instance.
        Implements the IDestroyable interface.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"destroy: {resp.result}")
        # Call parent class dispose method to clean up object pool
        super().dispose()
