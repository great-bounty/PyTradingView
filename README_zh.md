# PyTradingView

<div align="center">
  <img src="assets/icon.png" alt="PyTradingView Logo" width="128"/>
</div>

<div align="center">

[![PyPI version](https://badge.fury.io/py/pytradingviewlib.svg)](https://badge.fury.io/py/pytradingviewlib)
[![Python](https://img.shields.io/pypi/pyversions/pytradingviewlib.svg)](https://pypi.org/project/pytradingviewlib/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

使用 Python 编写 TradinView 指标。✨使用 Python 与 TradingView 交互📈，就像使用 JavaScript 一样🚀🎉。TradingView Widget API 的 Python 客户端库。
⚠️ **提示:** 您需要下载并安装GUI-App,才能将你使用本库编写的技术指标正确的显示在TradingView图表上.您可以通过仓库的release模块下载合适的GUI-App软件版本.或者您也可以[直接点击下载GUI-App](https://github.com/great-bounty/PyTradingView/releases/tag/latest-app)
简体中文 | [English](README.md)

## 🌟 特性

- **🎯 完整的 TradingView API 支持**：完整的 TradingView Advanced Charts API Python 实现
- **📊 自定义指标**：使用 Python 构建和部署自定义技术指标
- **🎨 丰富的绘图工具**：支持 100+ 种形状类型（趋势线、箭头、图案等）
- **📈 实时数据集成**：自定义数据源接口，支持实时市场数据
- **⚡ 高性能**：异步架构，支持 WebSocket
- **🔧 简单配置**：Pythonic API 设计，配置直观
- **🎭 多图表支持**：同时管理多个图表
- **🌈 主题定制**：完整的主题和样式自定义
- **📦 模块化设计**：清晰的模块分离，高可维护性

---

<div align="center">

### 📚 **[访问我们的 Wiki 获取全面的文档资料](https://github.com/great-bounty/PyTradingView/wiki)**

*需要详细的指南、API 参考和高级教程？我们的 Wiki 提供了涵盖 PyTradingView 各个方面的详尽文档，从安装到高级功能应有尽有。*

**[🔗 访问 Wiki 文档 →](https://github.com/great-bounty/PyTradingView/wiki)**

</div>

---

## 📋 要求

- Python >= 3.8
- TradingView Advanced Charts 库
- 支持 JavaScript 的现代浏览器

## 🚀 安装

### 从 PyPI 安装

```bash
pip install pytradingviewlib
```

### 从源码安装

```bash
git clone https://github.com/great-bounty/pytradingview.git
cd pytradingview
pip install -e .
```

### 开发环境安装

```bash
pip install -e ".[dev]"
```

## 📖 快速开始

### 基本使用

```python
from pytradingview import TVEngine

if __name__ == '__main__':
    # 初始化引擎
    engine = TVEngine()
    
    # 设置并运行自定义指标
    engine.get_instance().setup('./indicators').run()
```

### 创建自定义指标

```python
from pytradingview.indicators import (
    TVIndicator,
    TVSignal,
    TVDrawable,
    IndicatorConfig,
    InputType,
    InputDefinition,
    register_indicator
)
import pandas as pd
from typing import List, Tuple

@register_indicator(name="MyIndicator", enabled=True)
class MyCustomIndicator(TVIndicator):
    """
    自定义指标示例
    """
    
    def get_config(self) -> IndicatorConfig:
        """定义指标配置"""
        return IndicatorConfig(
            name="我的自定义指标",
            version="1.0.0",
            description="一个简单的自定义指标",
            author="你的名字",
            enabled=True,
            inputs=[
                InputDefinition(
                    id="period",
                    display_name="周期",
                    type=InputType.INTEGER,
                    default_value=14,
                    min_value=1,
                    max_value=100
                )
            ]
        )
    
    def calculate(self, df: pd.DataFrame) -> Tuple[List[TVSignal], List[TVDrawable]]:
        """计算指标信号"""
        signals = []
        drawables = []
        
        # 你的指标逻辑
        # ...
        
        return signals, drawables
```

### 操作图表

```python
from pytradingview import TVWidget, TVChart

# 获取 widget 实例

widget = TVWidget.get_instance("widget_id")

# 获取当前活动图表
chart = await widget.activeChart()

# 在图表上创建形状
from pytradingview.shapes import TVTrendLine, TVShapePoint

trend_line = TVTrendLine()
await chart.createMultipointShape(
    points=[
        TVShapePoint(time=1234567890, price=50000),
        TVShapePoint(time=1234567900, price=51000)
    ],
    shape=trend_line
)
```

### 自定义数据源

```python
from pytradingview.datafeed import (
    TVDatafeed,
    TVLibrarySymbolInfo,
    TVBar,
    TVHistoryMetadata
)

class MyDatafeed(TVDatafeed):
    """自定义数据源实现"""
    
    def resolveSymbol(self, symbolName, onResolve, onError, extension=None):
        """解析交易对信息"""
        symbol_info = TVLibrarySymbolInfo(
            name=symbolName,
            ticker=symbolName,
            description=f"{symbolName} 描述",
            type="crypto",
            session="24x7",
            exchange="MyExchange",
            listed_exchange="MyExchange",
            timezone="Etc/UTC",
            format="price",
            pricescale=100,
            minmov=1,
            has_intraday=True,
            supported_resolutions=["1", "5", "15", "60", "D", "W", "M"]
        )
        onResolve(symbol_info)
    
    def getBars(self, symbolInfo, resolution, periodParams, onResult, onError):
        """获取历史K线数据"""
        # 在这里获取你的数据
        bars = [
            TVBar(
                time=1234567890000,  # 毫秒
                open=50000,
                high=51000,
                low=49000,
                close=50500,
                volume=1000
            ),
            # ... 更多 K 线
        ]
        
        metadata = TVHistoryMetadata(noData=False)
        onResult(bars, metadata)
```

## 📚 核心组件

### 核心模块 (`pytradingview.core`)

- **TVWidget**：主控件控制器
- **TVChart**：图表 API 接口
- **TVBridge**：Python-JavaScript 桥接
- **TVObject**：基础对象类
- **TVSubscription**：事件订阅管理器

### 指标模块 (`pytradingview.indicators`)

- **TVEngine**：指标引擎（单例模式）
- **TVIndicator**：自定义指标基类
- **IndicatorConfig**：配置管理
- **TVSignal**：交易信号数据结构
- **TVDrawable**：绘图元素数据结构
- **IndicatorRegistry**：指标注册系统

### 形状模块 (`pytradingview.shapes`)

100+ 种绘图形状，包括：
- 线条：`TVTrendLine`、`TVHorizontalLine`、`TVVerticalLine`
- 箭头：`TVArrowUp`、`TVArrowDown`、`TVArrow`
- 图案：`TVTriangle`、`TVRectangle`、`TVEllipse`
- 斐波那契：`TVFibRetracement`、`TVFibChannel`
- 还有更多...

### 数据源模块 (`pytradingview.datafeed`)

- **TVDatafeed**：数据源基类
- **TVLibrarySymbolInfo**：交易对信息
- **TVBar**：OHLCV K线数据
- **Callbacks**：完整的回调接口

## 🎨 高级功能

### 多图表布局

```python
# 获取图表数量
count = await widget.chartsCount()

# 获取指定图表
chart = await widget.chart(index=0)

# 获取当前活动图表
active_chart = await widget.activeChart()
```

### 主题定制

```python
# 切换主题
await widget.changeTheme("dark")

# 应用自定义覆盖
await widget.applyOverrides({
    "mainSeriesProperties.candleStyle.upColor": "#26a69a",
    "mainSeriesProperties.candleStyle.downColor": "#ef5350"
})
```

### 事件处理

```python
# 订阅图表事件
await chart.onIntervalChanged(callback=my_interval_handler)

# 订阅交易对变化
await chart.onSymbolChanged(callback=my_symbol_handler)
```

## 📊 示例项目

查看 `examples/` 目录获取完整的工作示例：

- **False Breakout Indicator**：带自定义绘图的高级指标
- **Basic Engine Setup**：简单的引擎初始化
- **Custom Datafeed**：实时数据集成

## 🛠️ 开发

### 项目结构

```
pytradingview/
├── core/              # 核心 widget 和 chart API
├── datafeed/          # 数据源接口
├── indicators/        # 指标引擎和基类
│   └── engine/       # 模块化引擎组件
├── shapes/            # 绘图形状 (100+ 种类型)
├── models/            # 数据模型
├── server/            # Web 服务器
├── trading/           # 交易接口
├── ui/                # UI 组件
└── utils/             # 工具函数
```

### 运行测试

```bash
pytest tests/
```

### 代码质量

```bash
# 格式化代码
black pytradingview/

# 代码检查
ruff check pytradingview/

# 类型检查
mypy pytradingview/
```

## 🤝 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解我们的行为准则和提交 Pull Request 的流程。

## 📝 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本历史和发布说明。

## 📄 许可证

该项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 感谢 TradingView 提供的优秀图表库
- 感谢 Python 社区提供的优秀工具和库
- 感谢所有帮助改进这个项目的贡献者

## 📮 支持

- **问题反馈**：[GitHub Issues](https://github.com/great-bounty/pytradingview/issues)
- **文档**：[Read the Docs](https://pytradingview.readthedocs.io)
- **讨论**：[GitHub Discussions](https://github.com/great-bounty/pytradingview/discussions)

## 📞 联系我们

欢迎通过以下任何方式与我们联系：

### 微信 (WeChat)
<div align="center">
  <img src="assets/wechat_qrcode.png" alt="微信二维码" width="200"/>
  <p><em>扫码添加微信</em></p>
</div>

### WhatsApp
<div align="center">
  <img src="assets/whatsapp_qrcode.png" alt="WhatsApp二维码" width="200"/>
  <p><em>扫码WhatsApp联系</em></p>
</div>

### 邮箱 (Email)
📧 **1531724247@qq.com**

## 🔗 链接

- [PyPI 包](https://pypi.org/project/pytradingviewlib/)
- [GitHub 仓库](https://github.com/great-bounty/pytradingview)
- [文档](https://pytradingview.readthedocs.io)
- [TradingView Charting Library](https://www.tradingview.com/charting-library/)

---

**由 PyTradingView 团队使用 ❤️ 打造**