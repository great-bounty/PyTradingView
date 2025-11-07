# PyTradingView

<div align="center">
  <img src="assets/icon.png" alt="PyTradingView Logo" width="128"/>
</div>

<div align="center">

[![PyPI version](https://badge.fury.io/py/pytradingviewlib.svg)](https://badge.fury.io/py/pytradingviewlib)
[![Python](https://img.shields.io/pypi/pyversions/pytradingviewlib.svg)](https://pypi.org/project/pytradingviewlib/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

Write TradingView indicators by Python! ✨Using Python to interact with TradingView📈, just like using JavaScript🚀🎉. A Python client library for TradingView Widget API.
⚠️ **Tips:** You need to download and install the GUI app in order to correctly display the technical indicators you write using this library on TradingView charts. You can download the appropriate version of the GUI app from the repository's Releases section.Alternatively, you can also click directly to [download the GUI app.](https://github.com/great-bounty/PyTradingView/releases/tag/latest-app)

[简体中文](README_zh.md) | English

## 🌟 Features

- **🎯 Full TradingView API Support**: Complete Python implementation of TradingView Advanced Charts API
- **📊 Custom Indicators**: Build and deploy custom technical indicators with Python
- **🎨 Rich Drawing Tools**: Support for 100+ shape types (trendlines, arrows, patterns, etc.)
- **📈 Real-time Data Integration**: Custom datafeed interface for real-time market data
- **⚡ High Performance**: Asynchronous architecture with WebSocket support
- **🔧 Easy Configuration**: Pythonic API design with intuitive configuration
- **🎭 Multi-Chart Support**: Manage multiple charts simultaneously
- **🌈 Theme Customization**: Full theme and styling customization
- **📦 Modular Design**: Clean separation of concerns with modular architecture

---

<div align="center">

### 📚 **[Visit Our Wiki for Comprehensive Documentation](https://github.com/great-bounty/PyTradingView/wiki)**

*Looking for detailed guides, API references, and advanced tutorials? Our Wiki provides extensive documentation covering all aspects of PyTradingView, from installation to advanced features.*

**[🔗 Explore the Wiki →](https://github.com/great-bounty/PyTradingView/wiki)**

</div>

---

## 📋 Requirements

- Python >= 3.8
- TradingView Advanced Charts library
- Modern web browser with JavaScript support

## 🚀 Installation

### Install from PyPI

```bash
pip install pytradingviewlib
```

### Install from Source

```bash
git clone https://github.com/great-bounty/pytradingview.git
cd pytradingview
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## 📖 Quick Start

### Basic Usage

```python
from pytradingview import TVEngine

if __name__ == '__main__':
    # Initialize the engine
    engine = TVEngine()
    
    # Setup and run with custom indicators
    engine.get_instance().setup('./indicators').run()
```

### Creating Custom Indicators

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
    Custom indicator example
    """
    
    def get_config(self) -> IndicatorConfig:
        """Define indicator configuration"""
        return IndicatorConfig(
            name="My Custom Indicator",
            version="1.0.0",
            description="A simple custom indicator",
            author="Your Name",
            enabled=True,
            inputs=[
                InputDefinition(
                    id="period",
                    display_name="Period",
                    type=InputType.INTEGER,
                    default_value=14,
                    min_value=1,
                    max_value=100
                )
            ]
        )
    
    def calculate(self, df: pd.DataFrame) -> Tuple[List[TVSignal], List[TVDrawable]]:
        """Calculate indicator signals"""
        signals = []
        drawables = []
        
        # Your indicator logic here
        # ...
        
        return signals, drawables
```

### Working with Charts

```python
from pytradingview import TVWidget, TVChart

# Get the widget instance
widget = TVWidget.get_instance("widget_id")

# Get active chart
chart = await widget.activeChart()

# Create a shape on the chart
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

### Custom Datafeed

```python
from pytradingview.datafeed import (
    TVDatafeed,
    TVLibrarySymbolInfo,
    TVBar,
    TVHistoryMetadata
)

class MyDatafeed(TVDatafeed):
    """Custom datafeed implementation"""
    
    def resolveSymbol(self, symbolName, onResolve, onError, extension=None):
        """Resolve symbol information"""
        symbol_info = TVLibrarySymbolInfo(
            name=symbolName,
            ticker=symbolName,
            description=f"{symbolName} Description",
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
        """Get historical bars"""
        # Fetch your data here
        bars = [
            TVBar(
                time=1234567890000,  # milliseconds
                open=50000,
                high=51000,
                low=49000,
                close=50500,
                volume=1000
            ),
            # ... more bars
        ]
        
        metadata = TVHistoryMetadata(noData=False)
        onResult(bars, metadata)
```

## 📚 Core Components

### Core Module (`pytradingview.core`)

- **TVWidget**: Main widget controller
- **TVChart**: Chart API interface
- **TVBridge**: Python-JavaScript bridge
- **TVObject**: Base object class
- **TVSubscription**: Event subscription manager

### Indicators Module (`pytradingview.indicators`)

- **TVEngine**: Indicator engine with singleton pattern
- **TVIndicator**: Base class for custom indicators
- **IndicatorConfig**: Configuration management
- **TVSignal**: Trading signal data structure
- **TVDrawable**: Drawing element data structure
- **IndicatorRegistry**: Indicator registration system

### Shapes Module (`pytradingview.shapes`)

100+ drawing shapes including:
- Lines: `TVTrendLine`, `TVHorizontalLine`, `TVVerticalLine`
- Arrows: `TVArrowUp`, `TVArrowDown`, `TVArrow`
- Patterns: `TVTriangle`, `TVRectangle`, `TVEllipse`
- Fibonacci: `TVFibRetracement`, `TVFibChannel`
- And many more...

### Datafeed Module (`pytradingview.datafeed`)

- **TVDatafeed**: Base datafeed class
- **TVLibrarySymbolInfo**: Symbol information
- **TVBar**: OHLCV bar data
- **Callbacks**: Complete callback interface

## 🎨 Advanced Features

### Multi-Chart Layout

```python
# Get number of charts
count = await widget.chartsCount()

# Get specific chart
chart = await widget.chart(index=0)

# Get active chart
active_chart = await widget.activeChart()
```

### Theme Customization

```python
# Change theme
await widget.changeTheme("dark")

# Apply custom overrides
await widget.applyOverrides({
    "mainSeriesProperties.candleStyle.upColor": "#26a69a",
    "mainSeriesProperties.candleStyle.downColor": "#ef5350"
})
```

### Event Handling

```python
# Subscribe to chart events
await chart.onIntervalChanged(callback=my_interval_handler)

# Subscribe to symbol changes
await chart.onSymbolChanged(callback=my_symbol_handler)
```

## 📊 Example Projects

Check out the `examples/` directory for complete working examples:

- **False Breakout Indicator**: Advanced indicator with custom drawing
- **Basic Engine Setup**: Simple engine initialization
- **Custom Datafeed**: Real-time data integration

## 🛠️ Development

### Project Structure

```
pytradingview/
├── core/              # Core widget and chart APIs
├── datafeed/          # Datafeed interfaces
├── indicators/        # Indicator engine and base classes
│   └── engine/       # Modular engine components
├── shapes/            # Drawing shapes (100+ types)
├── models/            # Data models
├── server/            # Web server
├── trading/           # Trading interface
├── ui/                # UI components
└── utils/             # Utility functions
```

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Format code
black pytradingview/

# Lint code
ruff check pytradingview/

# Type checking
mypy pytradingview/
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and release notes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- TradingView for their excellent charting library
- The Python community for amazing tools and libraries
- All contributors who have helped improve this project

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/great-bounty/pytradingview/issues)
- **Documentation**: [Read the Docs](https://pytradingview.readthedocs.io)
- **Discussions**: [GitHub Discussions](https://github.com/great-bounty/pytradingview/discussions)

## 📞 Contact Us

Feel free to reach out through any of the following channels:

### WeChat
<div align="center">
  <img src="assets/wechat_qrcode.png" alt="WeChat QR Code" width="200"/>
  <p><em>Scan to add on WeChat</em></p>
</div>

### WhatsApp
<div align="center">
  <img src="assets/whatsapp_qrcode.png" alt="WhatsApp QR Code" width="200"/>
  <p><em>Scan to chat on WhatsApp</em></p>
</div>

### Email
📧 **1531724247@qq.com**

## 🔗 Links

- [PyPI Package](https://pypi.org/project/pytradingviewlib/)
- [GitHub Repository](https://github.com/great-bounty/pytradingview)
- [Documentation](https://pytradingview.readthedocs.io)
- [TradingView Charting Library](https://www.tradingview.com/charting-library/)

---

**Made with ❤️ by the PyTradingView team**