from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List

class TVExecutionLine(TVObject):
    """
    An API object used to control execution lines.
    Corresponds to the IExecutionLineAdapter interface in TypeScript.
    """
    
    async def remove(self) -> None:
        """
        Remove the execution line. This API object cannot be used after this call.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def getPrice(self) -> float:
        """
        Get the price of the execution line.
        
        :return: The price of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setPrice(self, value: float) -> None:
        """
        Set the price of the execution line.
        
        :param value: The new price
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getTime(self) -> int:
        """
        Get the time of the execution line.
        
        :return: The time of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTime(self, value: int) -> None:
        """
        Set the time of the execution line.
        
        :param value: The new time
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getDirection(self) -> Any:
        """
        Get the direction of the execution line.
        
        :return: The direction of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setDirection(self, value: Any) -> None:
        """
        Set the direction of the execution line.
        
        :param value: The new direction
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getText(self) -> str:
        """
        Get the text of the execution line.
        
        :return: The text of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setText(self, value: str) -> None:
        """
        Set the text of the execution line.
        
        :param value: The new text
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getTooltip(self) -> str:
        """
        Get the tooltip of the execution line.
        
        :return: The tooltip of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTooltip(self, value: str) -> None:
        """
        Set the tooltip of the execution line.
        
        :param value: The new tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getArrowHeight(self) -> int:
        """
        Get the arrow height of the execution line.
        
        :return: The arrow height of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setArrowHeight(self, value: int) -> None:
        """
        Set the arrow height of the execution line.
        
        :param value: The new arrow height
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getArrowSpacing(self) -> int:
        """
        Get the arrow spacing of the execution line.
        
        :return: The arrow spacing of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setArrowSpacing(self, value: int) -> None:
        """
        Set the arrow spacing of the execution line.
        
        :param value: The new arrow spacing
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getFont(self) -> str:
        """
        Get the font of the execution line.
        
        :return: The font of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setFont(self, value: str) -> None:
        """
        Set the font of the execution line.
        
        :param value: The new font
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getTextColor(self) -> str:
        """
        Get the text color of the execution line.
        
        :return: The text color of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTextColor(self, value: str) -> None:
        """
        Set the text color of the execution line.
        
        :param value: The new text color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getArrowColor(self) -> str:
        """
        Get the arrow color of the execution line.
        
        :return: The arrow color of the execution line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setArrowColor(self, value: str) -> None:
        """
        Set the arrow color of the execution line.
        
        :param value: The new arrow color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )
