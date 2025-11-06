from typing import Any, Dict, Optional
import sys
import logging

from .TVBridgeObject import TVMethodResponse
from .TVObject import TVObject, CallBackParams

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


CustomThemes = Dict[str, Any]


class TVCustomThemes(TVObject):
    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def applyCustomThemes(
        self, customThemes: CustomThemes, callback: Optional[CallBackParams] = None
    ) -> None:
        self.applyCustomThemes_callback: Optional[CallBackParams] = callback

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"customThemes": customThemes},
        )
        logger.info(f"applyCustomThemes completed")

    async def applyCustomThemesCallback(self) -> None:
        logger.info("applyCustomThemesCallback: received from frontend")
        if (
            hasattr(self, "applyCustomThemes_callback")
            and self.applyCustomThemes_callback
        ):
            await self.handleCallbackFunction(callback=self.applyCustomThemes_callback)

    async def resetCustomThemes(
        self, callback: Optional[CallBackParams] = None
    ) -> None:
        self.resetCustomThemes_callback: Optional[CallBackParams] = callback

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"resetCustomThemes completed")

    async def resetCustomThemesCallback(self) -> None:
        logger.info("resetCustomThemesCallback: received from frontend")
        if (
            hasattr(self, "resetCustomThemes_callback")
            and self.resetCustomThemes_callback
        ):
            await self.handleCallbackFunction(callback=self.resetCustomThemes_callback)
