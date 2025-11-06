"""
Indicator Engine - Modular Refactored Version

Organize code using multi-layer inheritance to improve maintainability:

Inheritance hierarchy:
TVEngineSingleton (Singleton Base Class)
    ↓
TVEngineLoader (Module Loading)
    ↓
TVEngineManager (Indicator Management)
    ↓
TVEngineConfig (Configuration Management)
    ↓  
TVEngineRemote (Remote Call)
    ↓
TVEngineDrawing (Drawing Functionality)
    ↓
TVEngineRuntime (Runtime/Entry Point)
    ↓
TVEngine (Final Class, External Interface)
"""

from typing import Optional

from .engine.runtime_mixin import TVEngineRuntime


class TVEngine(TVEngineRuntime):
    """
    Indicator Engine (Modular Refactored Version)
    
    Functional modules:
    1. Singleton Management - TVEngineSingleton
    2. Module Loading - TVEngineLoader
    3. Indicator Management - TVEngineManager
    4. Configuration Management - TVEngineConfig
    5. Remote Call - TVEngineRemote
    6. Drawing Functionality - TVEngineDrawing
    7. Runtime Control - TVEngineRuntime
    
    Core features:
    - Singleton pattern: Ensures global unique instance
    - Thread safety: Uses lock mechanism to ensure concurrent safety
    - Modular design: Each functional module is independently maintained
    - Dynamic configuration: Supports runtime configuration updates
    - Remote call: Complete Electron IPC support
    - Event-driven: Event communication based on EventBus
    
    Usage example:
        >>> # Get singleton instance
        >>> engine = TVEngine.get_instance()
        >>> 
        >>> # Configuration and execution
        >>> engine.setup('./indicators', config={'symbol': 'BTCUSDT'})
        >>> engine.run()
        >>> 
        >>> # Remote call
        >>> status = engine.remote_get_status()
        >>> success, error = engine.remote_activate_indicator('FalseBreakout')
    """
    
    def __init__(self, config: Optional['TVWidgetConfig'] = None):  # type: ignore
        """
        Initialize indicator engine (only initializes on first call)
        
        Args:
            config: Widget configuration object (optional, will use default configuration)
            
        Note:
            Due to singleton pattern, repeated calls will not re-initialize
        """
        super().__init__(config)


# Backward compatibility: Maintain original import method
__all__ = ['TVEngine']
