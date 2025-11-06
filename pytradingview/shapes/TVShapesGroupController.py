from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List

class TVShapesGroupController(TVObject):
    async def createGroupFromSelection(self) -> Any:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def removeGroup(self, groupId: Any) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )

    async def groups(self) -> List[Any]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def shapesInGroup(self, groupId: Any) -> List[Any]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )
        return resp.result

    async def excludeShapeFromGroup(self, groupId: Any, shapeId: Any) -> None:
        kwargs = {"groupId": groupId, "shapeId": shapeId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def addShapeToGroup(self, groupId: Any, shapeId: Any) -> None:
        kwargs = {"groupId": groupId, "shapeId": shapeId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def availableZOrderOperations(self, groupId: Any) -> Dict[str, Any]:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )
        return resp.result

    async def bringToFront(self, groupId: Any) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )

    async def sendToBack(self, groupId: Any) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )

    async def bringForward(self, groupId: Any) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )

    async def sendBackward(self, groupId: Any) -> None:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )

    async def insertAfter(self, groupId: Any, target: Any) -> None:
        kwargs = {"groupId": groupId, "target": target}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def insertBefore(self, groupId: Any, target: Any) -> None:
        kwargs = {"groupId": groupId, "target": target}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def setGroupVisibility(self, groupId: Any, value: bool) -> None:
        kwargs = {"groupId": groupId, "value": value}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def groupVisibility(self, groupId: Any) -> Any:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )
        return resp.result

    async def setGroupLock(self, groupId: Any, value: bool) -> None:
        kwargs = {"groupId": groupId, "value": value}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def groupLock(self, groupId: Any) -> Any:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )
        return resp.result

    async def getGroupName(self, groupId: Any) -> str:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"groupId": groupId}
        )
        return resp.result

    async def setGroupName(self, groupId: Any, name: str) -> None:
        kwargs = {"groupId": groupId, "name": name}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )

    async def canBeGroupped(self, shapes: List[Any]) -> bool:
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"shapes": shapes}
        )
        return resp.result