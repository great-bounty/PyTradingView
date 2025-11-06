from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List

class TVTimezone(TVObject):
    async def availableTimezones(self) -> List[Any]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getTimezone(self) -> Any:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setTimezone(self, timezone: Any, options: Optional[Any] = None) -> None:
        kwargs: Dict[str, Any] = {"timezone": timezone, "options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def onTimezoneChanged(self) -> Any:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result