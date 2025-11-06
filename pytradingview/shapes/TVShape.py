from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List

class TVShape(TVObject):
    async def isSelectionEnabled(self) -> bool:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setSelectionEnabled(self, enable: bool) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enable": enable}
        )

    async def isSavingEnabled(self) -> bool:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setSavingEnabled(self, enable: bool) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enable": enable}
        )

    async def isShowInObjectsTreeEnabled(self) -> bool:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setShowInObjectsTreeEnabled(self, enabled: bool) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enabled": enabled}
        )

    async def isUserEditEnabled(self) -> bool:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setUserEditEnabled(self, enabled: bool) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enabled": enabled}
        )

    async def bringToFront(self) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def sendToBack(self) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def getProperties(self) -> Dict[str, Any]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setProperties(self, newProperties: object, saveDefaults: Optional[bool] = None) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"newProperties": newProperties, "saveDefaults": saveDefaults},
        )

    async def getPoints(self) -> List[Any]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setPoints(self, points: List[Any]) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"points": points}
        )

    async def getAnchoredPosition(self) -> Optional[Dict[str, float]]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setAnchoredPosition(self, positionPercents: Dict[str, float]) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"positionPercents": positionPercents}
        )