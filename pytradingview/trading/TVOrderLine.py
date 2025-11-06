from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List

class TVOrderLine(TVObject):
    """
    An API object used to control order lines.
    Corresponds to the IOrderLineAdapter interface in TypeScript.
    """
    
    async def remove(self) -> None:
        """
        Remove the order line. This API object cannot be used after this call.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def onModify(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed when the order line is modified.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed when the order line is modified (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onModify", kwargs=kwargs
        )

    async def onMove(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed when the order line is moved.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed when the order line is moved (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onMove", kwargs=kwargs
        )

    async def onMoving(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed while the order line is being moved.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed while the order line is being moved (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onMoving", kwargs=kwargs
        )

    async def onCancel(self, data_or_callback: Any, callback: Optional[Any] = None) -> None:
        """
        Attach a callback to be executed when the order line is cancelled.
        
        :param data_or_callback: Either a callback function or data to be passed to the callback
        :param callback: Callback to be executed when the order line is cancelled (optional)
        """
        kwargs = {"callback": data_or_callback} if callback is None else {"data": data_or_callback, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name="onCancel", kwargs=kwargs
        )

    async def getPrice(self) -> float:
        """
        Get the price of the order line.
        
        :return: The price of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setPrice(self, value: float) -> None:
        """
        Set the price of the order line.
        
        :param value: The new price
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getText(self) -> str:
        """
        Get the text of the order line.
        
        :return: The text of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setText(self, value: str) -> None:
        """
        Set the text of the order line.
        
        :param value: The new text
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getTooltip(self) -> str:
        """
        Get the tooltip of the order line.
        
        :return: The tooltip of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTooltip(self, value: str) -> None:
        """
        Set the tooltip of the order line.
        
        :param value: The new tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getModifyTooltip(self) -> str:
        """
        Get the modify tooltip of the order line.
        
        :return: The modify tooltip of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setModifyTooltip(self, value: str) -> None:
        """
        Set the modify tooltip of the order line.
        
        :param value: The new modify tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCancelTooltip(self) -> str:
        """
        Get the cancel tooltip of the order line.
        
        :return: The cancel tooltip of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCancelTooltip(self, value: str) -> None:
        """
        Set the cancel tooltip of the order line.
        
        :param value: The new cancel tooltip
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantity(self) -> str:
        """
        Get the quantity of the order line.
        
        :return: The quantity of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantity(self, value: str) -> None:
        """
        Set the quantity of the order line.
        
        :param value: The new quantity
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getEditable(self) -> bool:
        """
        Get the editable flag value of the order line.
        
        :return: The editable flag value of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setEditable(self, value: bool) -> None:
        """
        Set the editable of the order line.
        
        :param value: The new editable
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCancellable(self) -> bool:
        """
        Get the cancellable flag value of the order line.
        
        :return: The cancellable flag value of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCancellable(self, value: bool) -> None:
        """
        Set the cancellable flag value of the order line.
        
        :param value: The new cancellable flag value
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getExtendLeft(self) -> bool:
        """
        Get the extend left flag value of the order line.
        
        :return: The extend left flag value of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setExtendLeft(self, value: bool) -> None:
        """
        Set the extend left flag value of the order line.
        
        :param value: The new extend left flag value
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getLineLength(self) -> float:
        """
        Get the line length of the order line.
        
        :return: The line length of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getLineLengthUnit(self) -> Any:
        """
        Get the unit of length specified for the line length of the order line.
        
        :return: The unit of length for the line length
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineLength(self, value: float, unit: Optional[Any] = None) -> None:
        """
        Set the line length of the order line.
        
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
        Get the line style of the order line.
        
        :return: The line style of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineStyle(self, value: int) -> None:
        """
        Set the line style of the order line.
        
        :param value: The new line style
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getLineWidth(self) -> int:
        """
        Get the line width of the order line.
        
        :return: The line width of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineWidth(self, value: int) -> None:
        """
        Set the line width of the order line.
        
        :param value: The new line width
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyFont(self) -> str:
        """
        Get the body font of the order line.
        
        :return: The body font of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyFont(self, value: str) -> None:
        """
        Set the body font of the order line.
        
        Example:
            widget.activeChart().createOrderLine().setPrice(170).setBodyFont("bold 12px Verdana")
        
        :param value: The new body font
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityFont(self) -> str:
        """
        Get the quantity font of the order line.
        
        :return: The quantity font of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityFont(self, value: str) -> None:
        """
        Set the quantity font of the order line.
        
        Example:
            widget.activeChart().createOrderLine().setPrice(170).setQuantityFont("bold 12px Verdana")
        
        :param value: The new quantity font
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getLineColor(self) -> str:
        """
        Get the line color of the order line.
        
        :return: The line color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setLineColor(self, value: str) -> None:
        """
        Set the line color of the order line.
        
        :param value: The new line color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyBorderColor(self) -> str:
        """
        Get the body border color of the order line.
        
        :return: The body border color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyBorderColor(self, value: str) -> None:
        """
        Set the body border color of the order line.
        
        :param value: The new body border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyBackgroundColor(self) -> str:
        """
        Get the body background color of the order line.
        
        :return: The body background color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyBackgroundColor(self, value: str) -> None:
        """
        Set the body background color of the order line.
        
        :param value: The new body background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getBodyTextColor(self) -> str:
        """
        Get the body text color of the order line.
        
        :return: The body text color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setBodyTextColor(self, value: str) -> None:
        """
        Set the body text color of the order line.
        
        :param value: The new body text color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityBorderColor(self) -> str:
        """
        Get the quantity border color of the order line.
        
        :return: The quantity border color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityBorderColor(self, value: str) -> None:
        """
        Set the quantity border color of the order line.
        
        :param value: The new quantity border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityBackgroundColor(self) -> str:
        """
        Get the quantity background color of the order line.
        
        :return: The quantity background color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityBackgroundColor(self, value: str) -> None:
        """
        Set the quantity background color of the order line.
        
        :param value: The new quantity background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getQuantityTextColor(self) -> str:
        """
        Get the quantity text color of the order line.
        
        :return: The quantity text color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setQuantityTextColor(self, value: str) -> None:
        """
        Set the quantity text color of the order line.
        
        :param value: The new quantity text color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCancelButtonBorderColor(self) -> str:
        """
        Get the cancel button border color of the order line.
        
        :return: The cancel button border color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCancelButtonBorderColor(self, value: str) -> None:
        """
        Set the cancel button border color of the order line.
        
        :param value: The new cancel button border color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCancelButtonBackgroundColor(self) -> str:
        """
        Get the cancel button background color of the order line.
        
        :return: The cancel button background color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCancelButtonBackgroundColor(self, value: str) -> None:
        """
        Set the cancel button background color of the order line.
        
        :param value: The new cancel button background color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )

    async def getCancelButtonIconColor(self) -> str:
        """
        Get the cancel button icon color of the order line.
        
        :return: The cancel button icon color of the order line
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setCancelButtonIconColor(self, value: str) -> None:
        """
        Set the cancel button icon color of the order line.
        
        :param value: The new cancel button icon color
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"value": value}
        )