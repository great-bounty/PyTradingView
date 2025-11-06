from typing import Any, List, Union
import sys
import logging

from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject
from ..core.TVSubscription import TVSubscription

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 类型别名
EntityId = str


class TVSelection(TVObject):
    """
    TradingView Selection API Python 端实现
    对应前端的 ISelectionApi 接口
    """

    def __init__(self, object_id: str = ""):
        super().__init__(object_id)

    async def add(self, entities: Union[List[EntityId], EntityId]) -> None:
        """
        将实体/实体组添加到选择中
        :param entities: 要添加到选择的实体（单个或数组）
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"entities": entities}
        )
        logger.info(f"add: {resp.result}")

    async def set(self, entities: Union[List[EntityId], EntityId]) -> None:
        """
        将实体/实体组设置为选择
        :param entities: 要选择的实体（单个或数组）
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"entities": entities}
        )
        logger.info(f"set: {resp.result}")

    async def remove(self, entities: List[EntityId]) -> None:
        """
        从选择中移除实体
        :param entities: 要从选择中移除的实体数组
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"entities": entities}
        )
        logger.info(f"remove: {resp.result}")

    async def contains(self, entity: EntityId) -> bool:
        """
        检查选择是否包含该实体
        :param entity: 要检查的实体
        :return: 当实体在选择中时返回 True
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"entity": entity}
        )
        return resp.result

    async def allSources(self) -> List[EntityId]:
        """
        返回选择中的所有实体
        :return: 实体 ID 数组
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def isEmpty(self) -> bool:
        """
        检查选择是否为空
        :return: 当选择为空时返回 True
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def clear(self) -> None:
        """
        清空选择
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"clear: {resp.result}")

    async def onChanged(self) -> TVSubscription:
        """
        订阅选择变更事件
        :return: 选择变更的订阅对象
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVSubscription.get_or_create(object_id=resp.result)

    async def canBeAddedToSelection(self, entity: EntityId) -> bool:
        """
        检查实体是否可以添加到选择中
        :param entity: 要检查的实体
        :return: 当实体可以添加到选择中时返回 True
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"entity": entity}
        )
        return resp.result
