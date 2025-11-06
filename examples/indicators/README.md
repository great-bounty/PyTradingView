# False Breakout Indicator 实现说明

## 概述

本目录包含基于 TradingView Pine Script 的 False Breakout 指标的 Python 实现。该指标用于检测虚假突破模式，即价格突破新高/新低后快速反转的情况。

## 文件结构

```
indicators/
├── __init__.py                      # 模块初始化
├── false_breakout_indicator.py      # 虚假突破指标实现
└── README.md                        # 本文档
```

## 指标说明

### False Breakout Indicator (虚假突破检测)

**原作者**: Zeiierman  
**许可证**: CC BY-NC-SA 4.0  
**Python实现**: 基于项目架构规范的完整实现

### 核心算法

虚假突破检测基于以下逻辑：

1. **新高/新低检测**
   - 计算指定周期内的最高价和最低价
   - 检测价格是否创造新的高点或低点
   
2. **状态追踪**
   - 维护计数器追踪连续的新高/新低
   - 记录触发价格和索引位置
   
3. **突破确认**
   - 检测价格是否反向突破触发价格
   - 验证最小周期和最大有效期条件
   
4. **信号生成**
   - 虚假突破向上：价格突破新低后反弹（卖出信号）
   - 虚假突破向下：价格突破新高后回落（买入信号）

### 配置参数

#### 主要设置 (Main Settings)

| 参数 | 类型 | 默认值 | 范围 | 说明 |
|------|------|--------|------|------|
| `period` | 整数 | 20 | 2-100 | 新高/新低检测周期 |
| `min_period` | 整数 | 5 | 0-100 | 最小突破间隔（K线数） |
| `max_period` | 整数 | 5 | 1-100 | 信号有效期（K线数） |

#### 高级平滑 (Advanced Smoothing)

| 参数 | 类型 | 默认值 | 选项 | 说明 |
|------|------|--------|------|------|
| `ma_type` | 选项 | "💎" | 💎/WMA/HMA | 平滑算法类型 |
| `ma_length` | 整数 | 10 | 1-100 | 平滑周期 |
| `aggressive` | 布尔 | False | - | 激进模式开关 |

### 样式配置

#### 虚假突破向上 (False Breakout Up)
- **颜色**: #f23645 (红色)
- **线宽**: 2
- **线型**: 实线
- **显示**: 三角形向下箭头 + 水平线

#### 虚假突破向下 (False Breakout Down)
- **颜色**: #6ce5a0 (绿色)
- **线宽**: 2
- **线型**: 实线
- **显示**: 三角形向上箭头 + 水平线

## 架构设计

### 类继承结构

```
TVIndicator (基类)
    ↓
FalseBreakoutIndicator (实现类)
```

### 核心组件

1. **FalseBreakoutState**
   - 数据类，用于追踪指标状态
   - 包含计数器、触发价格、索引记录

2. **FalseBreakoutIndicator**
   - 继承自 `TVIndicator`
   - 实现 `get_config()` - 返回配置
   - 实现 `calculate()` - 执行计算
   - 使用 `@register_indicator` 自动注册

### 数据流

```
输入数据 (DataFrame)
    ↓
参数获取 (IndicatorConfig)
    ↓
数据预处理 (numpy arrays)
    ↓
平滑处理 (WMA/HMA/None)
    ↓
新高/新低检测
    ↓
状态更新与追踪
    ↓
突破条件判断
    ↓
信号生成 (TVSignal)
    ↓
图形生成 (TVDrawable)
    ↓
输出结果
```

## 使用示例

### 基本使用

```python
from pytradingview.indicators import TVEngine
from indicators.false_breakout_indicator import FalseBreakoutIndicator
import pandas as pd

# 创建指标实例
indicator = FalseBreakoutIndicator()

# 准备数据
df = pd.DataFrame({
    'time': [...],      # UNIX时间戳（秒）
    'open': [...],
    'high': [...],
    'low': [...],
    'close': [...],
    'volume': [...]
})

# 计算信号
signals, drawables = indicator.calculate(df)

# 处理结果
for signal in signals:
    print(f"{signal.signal_type} at {signal.price}")
```

### 参数配置

```python
# 获取配置
config = indicator.get_config()

# 修改单个参数
indicator.update_input_value('period', 30)
indicator.update_input_value('aggressive', True)

# 批量修改
config.set_input_values({
    'period': 30,
    'min_period': 3,
    'max_period': 10
})

# 重新计算
signals, drawables = indicator.calculate(df)
```

### 样式定制

```python
# 修改颜色
indicator.update_style('false_breakout_up', 
                       color='#FF0000', 
                       line_width=3)

indicator.update_style('false_breakout_down',
                       color='#00FF00',
                       line_width=3)
```

### 与引擎集成

```python
from pytradingview.indicators import TVEngine

# 获取引擎实例
engine = TVEngine.get_instance()

# 指标已通过装饰器自动注册
# 可以直接激活使用
success, error = engine.remote_activate_indicator('FalseBreakout')
```

## 技术细节

### 平滑算法实现

#### WMA (加权移动平均)
```python
def _wma(self, data, length):
    weights = np.arange(1, length + 1)
    result = np.sum(window * weights) / np.sum(weights)
    return result
```

#### HMA (Hull移动平均)
```python
def _hma(self, data, length):
    # 1. 计算WMA(n)和WMA(n/2)
    wma_full = wma(data, length)
    wma_half = wma(data, length // 2)
    
    # 2. 计算2*WMA(n/2) - WMA(n)
    raw_hma = 2 * wma_half - wma_full
    
    # 3. 对结果应用WMA(sqrt(n))
    return wma(raw_hma, int(sqrt(length)))
```

### 时间戳处理

指标使用 UNIX 时间戳（秒）：
- 输入：DataFrame 的 `time` 列（秒）
- 输出：`TVSignal.timestamp` 和 `TVDrawable.points` 使用秒级时间戳
- 优势：与 TradingView API 完全兼容，无需转换

### 性能优化

1. **使用NumPy数组**
   - 避免逐行DataFrame操作
   - 利用向量化计算
   
2. **滚动窗口优化**
   - 最高/最低价计算使用切片
   - 避免重复计算
   
3. **条件短路**
   - 提前检查空值和边界条件
   - 减少不必要的计算

## 测试

运行示例脚本：

```bash
cd examples
python example_false_breakout.py
```

输出包括：
- 生成的K线数据统计
- 检测到的虚假突破信号
- 可绘制元素统计
- 参数修改演示
- 配置序列化演示

## 与Pine Script的对应关系

| Pine Script | Python 实现 | 说明 |
|-------------|-------------|------|
| `input.int()` | `InputDefinition(type=INTEGER)` | 整数参数 |
| `input.bool()` | `InputDefinition(type=BOOLEAN)` | 布尔参数 |
| `input.string()` | `InputDefinition(type=OPTIONS)` | 选项参数 |
| `ta.highest()` | `_calculate_highest()` | 最高价计算 |
| `ta.lowest()` | `_calculate_lowest()` | 最低价计算 |
| `ta.wma()` | `_wma()` | 加权移动平均 |
| `ta.hma()` | `_hma()` | Hull移动平均 |
| `ta.crossover()` | 自定义逻辑 | 向上穿越 |
| `ta.crossunder()` | 自定义逻辑 | 向下穿越 |
| `line.new()` | `TVDrawable + TVTrendLine` | 绘制线条 |
| `plotshape()` | `TVSignal + TVArrowUp/Down` | 绘制箭头 |
| `alertcondition()` | `TVSignal` | 警报条件 |

## 扩展开发

### 添加新功能

1. **自定义参数**
   ```python
   InputDefinition(
       id="my_param",
       display_name="My Parameter",
       type=InputType.INTEGER,
       default_value=10,
       # ...
   )
   ```

2. **新的绘图元素**
   ```python
   from pytradingview.shapes import TVCircle
   
   drawables.append(TVDrawable(
       points=[(time, price)],
       shape=TVCircle()
   ))
   ```

3. **自定义回调**
   ```python
   def on_calculate_end(self, signals, drawables):
       print(f"Generated {len(signals)} signals")
       super().on_calculate_end(signals, drawables)
   ```

## 常见问题

### Q: 如何调整灵敏度？
A: 减小 `min_period` 或增大 `max_period` 可以增加信号数量

### Q: 激进模式有什么作用？
A: 激进模式使用相反的价格进行检测（高价检测最低，低价检测最高），可能产生更多信号

### Q: 平滑算法如何选择？
A: 
- 💎 (无平滑): 最灵敏，信号最多
- WMA: 中等平滑
- HMA: 最平滑，延迟最小

### Q: 如何保存/加载配置？
A: 使用 `to_json()` 和 `from_json()` 方法

```python
# 保存
json_str = config.to_json()
with open('config.json', 'w') as f:
    f.write(json_str)

# 加载
with open('config.json', 'r') as f:
    json_str = f.read()
config.from_json(json_str)
```

## 许可证

本实现遵循原 Pine Script 的许可证：
**Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**

详见: https://creativecommons.org/licenses/by-nc-sa/4.0/

## 参考资料

- [TradingView Pine Script 文档](https://www.tradingview.com/pine-script-docs/)
- [项目架构文档](../../README.md)
- [Indicator 基类文档](../../pytradingview/indicators/indicator_base.py)
- [配置系统文档](../../pytradingview/indicators/indicator_config.py)
