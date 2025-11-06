"""
用户自定义指标模块

将你的自定义指标文件放在这个目录中，
指标引擎会自动发现并加载它们。
"""

# 导入自定义指标（使用@register_indicator装饰器自动注册）
from .false_breakout_indicator import FalseBreakoutIndicator

__all__ = [
    'FalseBreakoutIndicator',
]
