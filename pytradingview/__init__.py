"""PyTradingView - A Python client library for TradingView Widget API

This package provides a Pythonic interface to the TradingView Advanced Charts API,
allowing you to create and interact with TradingView charts programmatically.
"""

__version__ = "1.0.5"

# Core exports
from .core import (
    TVWidget,
    TVChart,
    TVBridge,
    TVObject,
    TVObjectPool,
    TVSubscription,
    TVSubscribeManager,
    TVWatchedValue,
)

# Indicator exports
from .indicators import (
    TVEngine,
    TVIndicator,
    IndicatorConfig,
    TVSignal,
    TVDrawable,
    IndicatorRegistry,
    register_indicator,
)

# Shape exports (commonly used)
from .shapes import TVShapePoint, TVShapePosition

__all__ = [
    "__version__",
    # Core
    "TVWidget",
    "TVChart",
    "TVBridge",
    "TVObject",
    "TVObjectPool",
    "TVSubscription",
    "TVSubscribeManager",
    "TVWatchedValue",
    # Indicators
    "TVEngine",
    "TVIndicator",
    "IndicatorConfig",
    "TVSignal",
    "TVDrawable",
    "IndicatorRegistry",
    "register_indicator",
    # Shapes
    "TVShapePoint",
    "TVShapePosition",
]
