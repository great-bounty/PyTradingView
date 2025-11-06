"""
False Breakout Indicator - 虚假突破检测指标

基于TradingView的False Breakout (Expo)指标的Python实现
原作者: Zeiierman
许可证: Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

该指标检测虚假突破，即价格突破新高/新低后快速反转的情况。
"""

from typing import List, Tuple, Optional
import pandas as pd
import numpy as np
from dataclasses import dataclass

from pytradingview.indicators import (
    TVIndicator,
    TVSignal,
    TVDrawable,
    IndicatorConfig,
    InputType,
    InputDefinition,
    StyleDefinition,
    InputOption,
    register_indicator
)
from pytradingview.shapes import TVTrendLine, TVArrowUp, TVArrowDown, TVShapePoint
from pytradingview.core import TVChart


@dataclass
class FalseBreakoutState:
    """虚假突破状态追踪"""
    count: int = 0  # 计数器：正数表示向上，负数表示向下
    val: float = 0.0  # 当前触发价格
    index: Optional[List[int]] = None  # 最近两次新高/新低的索引
    
    def __post_init__(self):
        if self.index is None:
            self.index = [0, 0]


@register_indicator(name="FalseBreakout", enabled=True)
class FalseBreakoutIndicator(TVIndicator):
    """
    虚假突破指标
    
    检测虚假突破模式：
    1. 价格创造新高/新低
    2. 在一定周期内再次创造新高/新低
    3. 价格反向突破触发价格
    4. 满足最小周期和最大有效周期条件
    """
    
    def get_config(self) -> IndicatorConfig:
        """返回指标配置"""
        return IndicatorConfig(
            name="False Breakout (Expo)",
            version="1.0.0",
            description="检测虚假突破模式，识别价格突破后快速反转的信号",
            author="Zeiierman (Python实现)",
            enabled=True,
            debug=False,
            
            inputs=[
                # 虚假突破周期
                InputDefinition(
                    id="period",
                    display_name="False Breakout Period",
                    type=InputType.INTEGER,
                    default_value=20,
                    min_value=2,
                    max_value=100,
                    tooltip="设置新高/新低的周期",
                    group="Main Settings"
                ),
                
                # 最小周期
                InputDefinition(
                    id="min_period",
                    display_name="New Breakout within minimum X bars",
                    type=InputType.INTEGER,
                    default_value=5,
                    min_value=0,
                    max_value=100,
                    tooltip="在最少X根K线内的新突破。低值返回更多假突破，高值返回更少",
                    group="Main Settings"
                ),
                
                # 信号有效期
                InputDefinition(
                    id="max_period",
                    display_name="Signal valid for X bars",
                    type=InputType.INTEGER,
                    default_value=5,
                    min_value=1,
                    max_value=100,
                    tooltip="设置虚假突破信号可以有效的周期数。高值返回更多信号，低值返回更少",
                    group="Main Settings"
                ),
                
                # 平滑类型
                InputDefinition(
                    id="ma_type",
                    display_name="Select Smoothing",
                    type=InputType.OPTIONS,
                    default_value="💎",
                    options=[
                        InputOption("Diamond", "💎"),
                        InputOption("WMA", "WMA"),
                        InputOption("HMA", "HMA")
                    ],
                    tooltip="设置平滑滤波器，帮助过滤某些信号",
                    group="Advanced Smoothing"
                ),
                
                # 平滑长度
                InputDefinition(
                    id="ma_length",
                    display_name="Smoothing Length",
                    type=InputType.INTEGER,
                    default_value=10,
                    min_value=1,
                    max_value=100,
                    tooltip="平滑周期",
                    group="Advanced Smoothing"
                ),
                
                # 激进模式
                InputDefinition(
                    id="aggressive",
                    display_name="Aggressive",
                    type=InputType.BOOLEAN,
                    default_value=False,
                    tooltip="启用更激进的虚假突破检测",
                    group="Advanced Smoothing"
                ),
            ],
            
            styles=[
                # 向上虚假突破样式
                StyleDefinition(
                    id="false_breakout_up",
                    display_name="False Breakout Up",
                    color="#f23645",
                    line_width=2,
                    line_style=0,
                    transparency=0,
                    visible=True,
                    group="Signals"
                ),
                
                # 向下虚假突破样式
                StyleDefinition(
                    id="false_breakout_down",
                    display_name="False Breakout Down",
                    color="#6ce5a0",
                    line_width=2,
                    line_style=0,
                    transparency=0,
                    visible=True,
                    group="Signals"
                ),
            ]
        )
    
    def calculate(self, df: pd.DataFrame) -> Tuple[List[TVSignal], List[TVDrawable]]:
        """
        计算虚假突破信号
        
        Args:
            df: 包含OHLC数据的DataFrame
            
        Returns:
            (signals, drawables): 信号列表和可绘制元素列表
        """
        if len(df) < 2:
            return [], []
        
        # 获取配置参数
        config = self.get_config()
        period = config.get_input_value("period")
        min_period = config.get_input_value("min_period")
        max_period = config.get_input_value("max_period")
        ma_type = config.get_input_value("ma_type")
        ma_length = config.get_input_value("ma_length")
        aggressive = config.get_input_value("aggressive")
        
        # 获取样式
        style_up = config.get_style("false_breakout_up")
        style_down = config.get_style("false_breakout_down")
        
        # 准备数据
        high = np.array(df['high'].values)
        low = np.array(df['low'].values)
        close = np.array(df['close'].values)
        time = df['time'].values if 'time' in df.columns else df.index.values
        
        # 计算最高价和最低价
        hi = self._calculate_highest(high if not aggressive else low, period)
        lo = self._calculate_lowest(low if not aggressive else high, period)
        
        # 应用平滑
        hi = self._apply_smoothing(hi, ma_type, ma_length)
        lo = self._apply_smoothing(lo, ma_type, ma_length)
        
        # 检测新高和新低条件
        cond_hi = np.zeros(len(df), dtype=bool)
        cond_lo = np.zeros(len(df), dtype=bool)
        
        for i in range(2, len(df)):
            cond_hi[i] = hi[i] > hi[i-1] and hi[i-1] <= hi[i-2]
            cond_lo[i] = lo[i] < lo[i-1] and lo[i-1] >= lo[i-2]
        
        # 状态追踪
        state = FalseBreakoutState()
        signals = []
        drawables = []
        
        for i in range(2, len(df)):
            # 新高检测
            if cond_hi[i]:
                if state.count > 0:
                    state.count = 0
                state.count -= 1
                state.val = low[i]
                if state.index is not None:
                    state.index = [i, state.index[0]]
            
            # 新低检测
            if cond_lo[i]:
                if state.count < 0:
                    state.count = 0
                state.count += 1
                state.val = high[i]
                if state.index is not None:
                    state.index = [i, state.index[0]]
            
            # 检查虚假突破条件
            if state.index is None:
                continue
                
            indx0 = state.index[0]
            indx1 = state.index[1]
            
            # 最小周期检查
            minbars = (indx1 + min_period) < indx0
            # 最大有效期检查
            maxvalid = (i - max_period) <= indx0
            
            # 突破检测
            breakdown = close[i] < state.val and (i > 0 and close[i-1] >= state.val)
            breakup = close[i] > state.val and (i > 0 and close[i-1] <= state.val)
            
            # 虚假突破向上（价格突破新低后反弹）
            if state.count < -1 and breakdown and maxvalid and minbars and style_up:
                # 创建信号
                signals.append(TVSignal(
                    signal_type='sell',
                    timestamp=int(time[i]),
                    price=float(high[i]),
                    metadata={
                        'style': {
                            'arrowColor': style_up.color,
                            'color': style_up.color,
                            'showLabel': True
                        }
                    }
                ))
                
                # 创建水平线
                if style_up.visible:
                    line_overrides = {
                        'line_color': style_up.color,
                        'line_width': style_up.line_width,
                        'line_style': style_up.line_style,
                        'show_price_labels': True,
                    }
                    
                    trend_line = TVTrendLine()
                    trend_line.overrides = line_overrides
                    
                    drawables.append(TVDrawable(
                        points=[
                            (int(time[indx0]), float(state.val)),
                            (int(time[i]), float(state.val))
                        ],
                        shape=trend_line,
                        metadata={'type': 'false_breakout_up'}
                    ))
                
                state.count = 0
            
            # 虚假突破向下（价格突破新高后回落）
            if state.count > 1 and breakup and maxvalid and minbars and style_down:
                # 创建信号
                signals.append(TVSignal(
                    signal_type='buy',
                    timestamp=int(time[i]),
                    price=float(low[i]),
                    metadata={
                        'style': {
                            'arrowColor': style_down.color,
                            'color': style_down.color,
                            'showLabel': True
                        }
                    }
                ))
                
                # 创建水平线
                if style_down.visible:
                    line_overrides = {
                        'line_color': style_down.color,
                        'line_width': style_down.line_width,
                        'line_style': style_down.line_style,
                        'show_price_labels': True,
                    }
                    
                    trend_line = TVTrendLine()
                    trend_line.overrides = line_overrides
                    
                    drawables.append(TVDrawable(
                        points=[
                            (int(time[indx0]), float(state.val)),
                            (int(time[i]), float(state.val))
                        ],
                        shape=trend_line,
                        metadata={'type': 'false_breakout_down'}
                    ))
                
                state.count = 0
        
        return signals, drawables
    
    def _calculate_highest(self, data: np.ndarray, period: int) -> np.ndarray:
        """计算滚动最高价"""
        result = np.zeros(len(data))
        for i in range(len(data)):
            start = max(0, i - period + 1)
            result[i] = np.max(data[start:i+1])
        return result
    
    def _calculate_lowest(self, data: np.ndarray, period: int) -> np.ndarray:
        """计算滚动最低价"""
        result = np.zeros(len(data))
        for i in range(len(data)):
            start = max(0, i - period + 1)
            result[i] = np.min(data[start:i+1])
        return result
    
    def _apply_smoothing(self, data: np.ndarray, ma_type: str, length: int) -> np.ndarray:
        """应用平滑算法"""
        if ma_type == "💎":
            return data
        elif ma_type == "WMA":
            return self._wma(data, length)
        elif ma_type == "HMA":
            return self._hma(data, length)
        return data
    
    def _wma(self, data: np.ndarray, length: int) -> np.ndarray:
        """加权移动平均"""
        result = np.zeros(len(data))
        weights = np.arange(1, length + 1)
        
        for i in range(len(data)):
            if i < length - 1:
                result[i] = data[i]
            else:
                window = data[i-length+1:i+1]
                result[i] = np.sum(window * weights) / np.sum(weights)
        
        return result
    
    def _hma(self, data: np.ndarray, length: int) -> np.ndarray:
        """Hull移动平均"""
        half_length = length // 2
        sqrt_length = int(np.sqrt(length))
        
        # 计算WMA
        wma_full = self._wma(data, length)
        wma_half = self._wma(data, half_length)
        
        # 2 * WMA(n/2) - WMA(n)
        raw_hma = 2 * wma_half - wma_full
        
        # 再对结果应用WMA(sqrt(n))
        return self._wma(raw_hma, sqrt_length)
