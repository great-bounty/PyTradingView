from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List

class TVPositionLine(TVObject):
    """
    An API object used to control position lines.
    Corresponds to the IPositionLineAdapter interface in TypeScript.
    """
    
    async def remove(self) -> None:
        """
        Remove the position line. This API object cannot be used after this call.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def onClose(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed when the position line is closed.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed when the position line is closed (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onClose", kwargs=kwargs
        )

    async def onModify(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed when the position line is modified.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed when the position line is modified (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onModify", kwargs=kwargs
        )

    async def onReverse(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed when the position line is reversed.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed when the position line is reversed (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onReverse", kwargs=kwargs
        )

    async def getPrice(self) -> float:
        """
        Get the price of the position line.
        
        :return: The price of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setPrice(self, value: float) -> None:
        """
        Set the price of the position line.
        
        :param value: The new price
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getText(self) -> str:
        """
        Get the text of the position line.
        
        :return: The text of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setText(self, value: str) -> None:
        """
        Set the text of the position line.
        
        :param value: The new text
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getTooltip(self) -> str:
        """
        Get the tooltip of the position line.
        
        :return: The tooltip of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTooltip(self, value: str) -> None:
        """
        Set the tooltip of the position line.
        
        :param value: The new tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getProtectTooltip(self) -> str:
        """
        Get the protect tooltip of the position line.
        
        :return: The protect tooltip of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setProtectTooltip(self, value: str) -> None:
        """
        Set the protect tooltip of the position line.
        
        :param value: The new protect tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCloseTooltip(self) -> str:
        """
        Get the close tooltip of the position line.
        
        :return: The close tooltip of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCloseTooltip(self, value: str) -> None:
        """
        Set the close tooltip of the position line.
        
        :param value: The new close tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getReverseTooltip(self) -> str:
        """
        Get the reverse tooltip of the position line.
        
        :return: The reverse tooltip of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setReverseTooltip(self, value: str) -> None:
        """
        Set the reverse tooltip of the position line.
        
        :param value: The new reverse tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantity(self) -> str:
        """
        Get the quantity of the position line.
        
        :return: The quantity of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantity(self, value: str) -> None:
        """
        Set the quantity of the position line.
        
        :param value: The new quantity
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getExtendLeft(self) -> bool:
        """
        Get the extend left flag value of the position line.
        
        :return: The extend left flag value of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setExtendLeft(self, value: bool) -> None:
        """
        Set the extend left flag value of the position line.
        
        :param value: The new extend left flag value
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getLineLengthUnit(self) -> Any:
        """
        Get the unit of length specified for the line length of the position line.
        
        :return: The unit of length for the line length
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getLineLength(self) -> float:
        """
        Get the line length of the position line.
        
        :return: The line length of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineLength(self, value: float, unit: Optional[Any] = None) -> None:
        """
        Set the line length of the position line.
        
        If negative number is provided for the value and the unit is 'pixel' then
        the position will be relative to the left edge of the chart.
        
        :param value: The new line length
        :param unit: Unit for the line length, defaults to 'percentage'
        """
        kwargs: Dict[str, Any] = {"value": value, "unit": unit}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def getLineStyle(self) -> int:
        """
        Get the line style of the position line.
        
        :return: The line style of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineStyle(self, value: int) -> None:
        """
        Set the line style of the position line.
        
        :param value: The new line style
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getLineWidth(self) -> int:
        """
        Get the line width of the position line.
        
        :return: The line width of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineWidth(self, value: int) -> None:
        """
        Set the line width of the position line.
        
        :param value: The new line width
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyFont(self) -> str:
        """
        Get the body font of the position line.
        
        :return: The body font of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyFont(self, value: str) -> None:
        """
        Set the body font of the position line.
        
        Example:
            widget.activeChart().createPositionLine().setPrice(170).setBodyFont("bold 12px Verdana")
        
        :param value: The new body font
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityFont(self) -> str:
        """
        Get the quantity font of the position line.
        
        :return: The quantity font of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityFont(self, value: str) -> None:
        """
        Set the quantity font of the position line.
        
        Example:
            widget.activeChart().createPositionLine().setPrice(170).setQuantityFont("bold 12px Verdana")
        
        :param value: The new quantity font
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getLineColor(self) -> str:
        """
        Get the line color of the position line.
        
        :return: The line color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineColor(self, value: str) -> None:
        """
        Set the line color of the position line.
        
        :param value: The new line color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyBorderColor(self) -> str:
        """
        Get the body border color of the position line.
        
        :return: The body border color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyBorderColor(self, value: str) -> None:
        """
        Set the body border color of the position line.
        
        :param value: The new body border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyBackgroundColor(self) -> str:
        """
        Get the body background color of the position line.
        
        :return: The body background color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyBackgroundColor(self, value: str) -> None:
        """
        Set the body background color of the position line.
        
        :param value: The new body background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyTextColor(self) -> str:
        """
        Get the body text color of the position line.
        
        :return: The body text color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyTextColor(self, value: str) -> None:
        """
        Set the body text color of the position line.
        
        :param value: The new body text color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityBorderColor(self) -> str:
        """
        Get the quantity border color of the position line.
        
        :return: The quantity border color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityBorderColor(self, value: str) -> None:
        """
        Set the quantity border color of the position line.
        
        :param value: The new quantity border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityBackgroundColor(self) -> str:
        """
        Get the quantity background color of the position line.
        
        :return: The quantity background color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityBackgroundColor(self, value: str) -> None:
        """
        Set the quantity background color of the position line.
        
        :param value: The new quantity background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityTextColor(self) -> str:
        """
        Get the quantity text color of the position line.
        
        :return: The quantity text color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityTextColor(self, value: str) -> None:
        """
        Set the quantity text color of the position line.
        
        :param value: The new quantity text color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getReverseButtonBorderColor(self) -> str:
        """
        Get the reverse button border color of the position line.
        
        :return: The reverse button border color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setReverseButtonBorderColor(self, value: str) -> None:
        """
        Set the reverse button border color of the position line.
        
        :param value: The new reverse button border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getReverseButtonBackgroundColor(self) -> str:
        """
        Get the reverse button background color of the position line.
        
        :return: The reverse button background color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setReverseButtonBackgroundColor(self, value: str) -> None:
        """
        Set the reverse button background color of the position line.
        
        :param value: The new reverse button background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getReverseButtonIconColor(self) -> str:
        """
        Get the reverse button icon color of the position line.
        
        :return: The reverse button icon color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setReverseButtonIconColor(self, value: str) -> None:
        """
        Set the reverse button icon color of the position line.
        
        :param value: The new reverse button icon color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCloseButtonBorderColor(self) -> str:
        """
        Get the close button border color of the position line.
        
        :return: The close button border color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCloseButtonBorderColor(self, value: str) -> None:
        """
        Set the close button border color of the position line.
        
        :param value: The new close button border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCloseButtonBackgroundColor(self) -> str:
        """
        Get the close button background color of the position line.
        
        :return: The close button background color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCloseButtonBackgroundColor(self, value: str) -> None:
        """
        Set the close button background color of the position line.
        
        :param value: The new close button background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCloseButtonIconColor(self) -> str:
        """
        Get the close button icon color of the position line.
        
        :return: The close button icon color of the position line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCloseButtonIconColor(self, value: str) -> None:
        """
        Set the close button icon color of the position line.
        
        :param value: The new close button icon color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )