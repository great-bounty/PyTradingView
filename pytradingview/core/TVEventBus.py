"""
事件总线 - 用于组件间解耦通信

职责：
- 管理事件订阅和发布
- 支持异步事件处理
- 提供类型安全的事件系统
"""

from typing import Dict, List, Callable, Any, Awaitable, Optional
import asyncio
import logging
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class EventType(str, Enum):
    """事件类型枚举"""
    # Widget 生命周期事件
    WIDGET_CREATED = "widget.created"
    WIDGET_READY = "widget.ready"
    WIDGET_DESTROYED = "widget.destroyed"
    
    # Chart 事件
    CHART_READY = "chart.ready"
    CHART_DATA_LOADED = "chart.data_loaded"
    CHART_DATA_EXPORTED = "chart.data_exported"
    
    # Indicator 事件
    INDICATOR_LOADED = "indicator.loaded"
    INDICATOR_ACTIVATED = "indicator.activated"
    INDICATOR_DEACTIVATED = "indicator.deactivated"
    INDICATOR_CALCULATED = "indicator.calculated"
    
    # Bridge 事件
    BRIDGE_STARTED = "bridge.started"
    BRIDGE_CONNECTED = "bridge.connected"
    BRIDGE_DISCONNECTED = "bridge.disconnected"


@dataclass
class Event:
    """事件数据结构"""
    type: EventType
    data: Dict[str, Any]
    source: Optional[str] = None
    
    def __repr__(self) -> str:
        return f"Event({self.type}, source={self.source})"


class EventBus:
    """
    事件总线 - 单例模式
    
    提供发布-订阅模式的事件系统，用于组件间解耦通信
    """
    
    _instance: Optional['EventBus'] = None
    
    @classmethod
    def get_instance(cls) -> 'EventBus':
        """获取单例实例"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        """初始化事件总线"""
        if EventBus._instance is not None:
            raise RuntimeError("EventBus is a singleton, use get_instance()")
        
        # 事件订阅者存储：{event_type: [callbacks]}
        self._subscribers: Dict[EventType, List[Callable]] = {}
        
        # 异步事件队列
        self._event_queue: asyncio.Queue = asyncio.Queue()
        
        # 是否正在运行
        self._running = False
    
    def subscribe(self, 
                  event_type: EventType, 
                  callback: Callable[[Event], Awaitable[None]]) -> None:
        """
        订阅事件
        
        Args:
            event_type: 事件类型
            callback: 异步回调函数
        """
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        
        self._subscribers[event_type].append(callback)
        logger.debug(f"Subscribed to {event_type}: {callback.__name__}")
    
    def unsubscribe(self, 
                    event_type: EventType, 
                    callback: Callable[[Event], Awaitable[None]]) -> None:
        """
        取消订阅
        
        Args:
            event_type: 事件类型
            callback: 要移除的回调函数
        """
        if event_type in self._subscribers:
            try:
                self._subscribers[event_type].remove(callback)
                logger.debug(f"Unsubscribed from {event_type}: {callback.__name__}")
            except ValueError:
                logger.warning(f"Callback not found for {event_type}")
    
    async def publish(self, 
                      event_type: EventType, 
                      data: Optional[Dict[str, Any]] = None,
                      source: Optional[str] = None) -> None:
        """
        发布事件（异步）
        
        Args:
            event_type: 事件类型
            data: 事件数据
            source: 事件源标识
        """
        event = Event(
            type=event_type,
            data=data or {},
            source=source
        )
        
        logger.debug(f"Publishing event: {event}")
        
        # 获取订阅者
        callbacks = self._subscribers.get(event_type, [])
        
        # 并发调用所有回调
        if callbacks:
            tasks = []
            for callback in callbacks:
                try:
                    tasks.append(callback(event))
                except Exception as e:
                    logger.error(f"Error creating task for {callback.__name__}: {e}")
            
            if tasks:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # 检查异常
                for i, result in enumerate(results):
                    if isinstance(result, Exception):
                        logger.error(
                            f"Error in event callback {callbacks[i].__name__}: {result}",
                            exc_info=result
                        )
    
    def publish_sync(self,
                     event_type: EventType,
                     data: Optional[Dict[str, Any]] = None,
                     source: Optional[str] = None) -> None:
        """
        发布事件（同步版本）
        
        在非异步上下文中使用
        
        Args:
            event_type: 事件类型
            data: 事件数据
            source: 事件源标识
        """
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # 如果事件循环正在运行，创建任务
                asyncio.create_task(self.publish(event_type, data, source))
            else:
                # 否则直接运行
                loop.run_until_complete(self.publish(event_type, data, source))
        except RuntimeError:
            # 没有事件循环，创建新的
            asyncio.run(self.publish(event_type, data, source))
    
    def clear_subscribers(self, event_type: Optional[EventType] = None) -> None:
        """
        清除订阅者
        
        Args:
            event_type: 要清除的事件类型，None 表示清除所有
        """
        if event_type is None:
            self._subscribers.clear()
            logger.info("Cleared all event subscribers")
        elif event_type in self._subscribers:
            del self._subscribers[event_type]
            logger.info(f"Cleared subscribers for {event_type}")
    
    def get_subscriber_count(self, event_type: EventType) -> int:
        """
        获取订阅者数量
        
        Args:
            event_type: 事件类型
            
        Returns:
            订阅者数量
        """
        return len(self._subscribers.get(event_type, []))
    
    def __repr__(self) -> str:
        total_subscribers = sum(len(subs) for subs in self._subscribers.values())
        return f"EventBus(events={len(self._subscribers)}, subscribers={total_subscribers})"
