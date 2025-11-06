"""
TVEngine Modular Architecture

Organize code using multi-layer inheritance:
1. TVEngineSingleton - Singleton base class
2. TVEngineLoader - Module loading
3. TVEngineManager - Indicator management (supports multi-chart)
4. TVEngineConfig - Configuration management
5. TVEngineRemote - Remote calls
6. TVEngineDrawing - Drawing functionality
7. TVEngineRuntime - Runtime
8. TVEngine - Final class
9. ChartContext - Chart context (multi-chart support)
"""

from .singleton_mixin import TVEngineSingleton
from .loader_mixin import TVEngineLoader
from .manager_mixin import TVEngineManager
from .config_mixin import TVEngineConfig
from .remote_mixin import TVEngineRemote
from .drawing_mixin import TVEngineDrawing
from .runtime_mixin import TVEngineRuntime
from .chart_context import ChartContext, ChartContextManager

__all__ = [
    'TVEngineSingleton',
    'TVEngineLoader',
    'TVEngineManager',
    'TVEngineConfig',
    'TVEngineRemote',
    'TVEngineDrawing',
    'TVEngineRuntime',
    'ChartContext',
    'ChartContextManager',
]
