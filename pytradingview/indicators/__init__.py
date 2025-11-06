"""Indicators module for PyTradingView."""

# Core classes
from .indicator_base import (
    TVIndicator,
    TVSignal,
    TVDrawable
)
from .indicator_config import (
    IndicatorConfig,
    InputType,
    InputOption,
    InputDefinition,
    StyleDefinition
)
from .indicator_registry import IndicatorRegistry, register_indicator
# Engine class - Using modular version
from .indicator_engine import TVEngine

__all__ = [
    # Core API
    "TVEngine",
    "TVIndicator",
    
    # Configuration system
    "IndicatorConfig",
    "InputType",
    "InputOption",
    "InputDefinition",
    "StyleDefinition",
    
    # Data structures
    "TVSignal",
    "TVDrawable",
    
    # Registration system
    "IndicatorRegistry",
    "register_indicator",
]
