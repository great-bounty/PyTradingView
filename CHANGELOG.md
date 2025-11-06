# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-06

### 🎉 Initial Release

This is the first stable release of PyTradingView - a comprehensive Python client library for TradingView Widget API.

### ✨ Added

#### Core Features
- **TVWidget**: Complete implementation of TradingView Widget API
  - Chart creation and management
  - Theme customization
  - Layout management
  - Event subscription system
  
- **TVChart**: Full chart API interface
  - Symbol and interval management
  - Study (indicator) operations
  - Shape and drawing tools
  - Time scale controls
  - Price scale controls

- **TVBridge**: Python-JavaScript bridge system
  - Bidirectional communication via WebSocket
  - Asynchronous method invocation
  - Event bus for real-time updates
  - Object lifecycle management

#### Indicator System
- **TVEngine**: Powerful indicator engine with singleton pattern
  - Modular architecture with 7 mixins
  - Dynamic indicator loading from directory
  - Real-time indicator activation/deactivation
  - Configuration management
  - Remote control interface
  
- **TVIndicator**: Base class for custom indicators
  - Lifecycle hooks (on_init, on_data_loaded, etc.)
  - Configuration system with inputs and styles
  - Signal generation (buy/sell/neutral)
  - Drawing element support
  - Auto-recalculation on config changes

- **IndicatorRegistry**: Indicator registration and discovery
  - Decorator-based registration
  - Metadata management
  - Enable/disable support

#### Drawing Tools
- **100+ Shape Types**: Comprehensive shape library
  - Lines: Trend, Horizontal, Vertical, Ray, Extended
  - Arrows: Up, Down, Left, Right, Markers
  - Patterns: Triangle, Rectangle, Ellipse, Circle
  - Fibonacci: Retracement, Extension, Channel, Spiral, Timezone
  - Gann: Box, Fan, Square
  - Elliott Wave: Impulse, Correction, Triangle, Combo
  - Pitchfork: Standard, Schiff, Modified, Inside
  - Anchored tools: VWAP, Text, Note
  - And many more...

- **Drawing API**: Unified drawing interface
  - Single-point shapes (arrows, notes, icons)
  - Multi-point shapes (lines, channels, patterns)
  - Style customization (color, width, transparency)
  - Position management (time-based coordinates)

#### Datafeed System
- **TVDatafeed**: Base datafeed implementation
  - Symbol search and resolution
  - Historical data (getBars)
  - Real-time data subscription
  - Quote data support
  - Mark and timescale mark support

- **Data Structures**: Complete TypeScript type mappings
  - TVBar (OHLCV data)
  - TVLibrarySymbolInfo (symbol metadata)
  - TVHistoryMetadata (pagination info)
  - TVQuoteData (real-time quotes)

#### Trading Interface
- **Order Management**:
  - TVOrderLine: Visual order representation
  - TVExecutionLine: Execution visualization
  - TVPositionLine: Position tracking

#### UI Components
- **TVContextMenuItem**: Custom context menu items
- **TVDropdownApi**: Dropdown menu controls
- **TVHMElement**: Toolbar button elements
- **TVWidgetbar**: Custom widget bars

#### Models & Data Structures
- **TVPane**: Chart pane management
- **TVSeries**: Price series data
- **TVStudy**: Indicator/study metadata
- **TVTimeScale**: Time axis controls
- **TVTimezone**: Timezone handling
- **TVExportedData**: Chart export functionality
- **TVNews**: News integration

#### Server
- **FastAPI Server**: Built-in web server
  - WebSocket support for bridge communication
  - Static file serving
  - CORS enabled
  - Development mode with auto-reload

### 🏗️ Architecture

- **Modular Design**: Clean separation of concerns
  - Core: Widget and chart APIs
  - Datafeed: Data integration layer
  - Indicators: Custom indicator system
  - Shapes: Drawing tools
  - Models: Data structures
  - Server: Web server
  - Trading: Trading interface
  - UI: UI components
  - Utils: Utility functions

- **Asynchronous**: Full async/await support
  - Non-blocking I/O operations
  - WebSocket-based communication
  - Efficient event handling

- **Type Safety**: Comprehensive type hints
  - Python 3.8+ type annotations
  - Runtime type validation
  - IDE autocomplete support

### 📚 Documentation

- **README.md**: Comprehensive English documentation
- **README_zh.md**: Complete Chinese documentation
- **Examples**: Working examples included
  - False Breakout Indicator
  - Basic engine setup
  - Custom indicator template

### 🛠️ Developer Tools

- **Code Quality**:
  - Black formatter configuration
  - Ruff linter setup
  - MyPy type checking
  - Pytest testing framework

- **Build System**:
  - Modern pyproject.toml configuration
  - Setuptools build backend
  - PyPI publishing ready

### 📦 Dependencies

- websocket-client >= 1.5.1
- fastapi >= 0.100.0
- uvicorn >= 0.23.0
- pandas >= 1.5.0
- aiohttp >= 3.8.0
- pathlib >= 1.0.1
- pandas-ta >= 0.4.71b0

### 🎯 Python Support

- Python 3.12

### 📄 License

- MIT License

---

## [Unreleased]

### Planned Features
- Enhanced documentation with more examples
- Additional built-in indicators
- Performance optimizations
- Extended datafeed adapters
- Real-time data streaming improvements
- Additional chart customization options

---

[1.0.1]: https://github.com/yourusername/pytradingview/releases/tag/v1.0.1
