"""
TVEngine Singleton Base Class
Provides thread-safe singleton pattern implementation
"""

import logging
import threading
from typing import Optional, TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from ...core.TVWidgetConfig import TVWidgetConfig

logger = logging.getLogger(__name__)


class TVEngineSingleton:
    """
    Indicator Engine Singleton Base Class
    
    Provides:
    - Thread-safe singleton pattern implementation
    - Instance initialization management
    - Singleton reset (for testing)
    """
    
    _instance: Optional['TVEngineSingleton'] = None
    _lock: Optional[threading.Lock] = None
    
    def __new__(cls, config: Optional['TVWidgetConfig'] = None):
        """
        Singleton pattern implementation (thread-safe)
        
        Args:
            config: Widget configuration object (only used on first creation)
        """
        if cls._lock is None:
            cls._lock = threading.Lock()
        
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False  # type: ignore
            return cls._instance
    
    @classmethod
    def get_instance(cls, config: Optional['TVWidgetConfig'] = None) -> 'TVEngineSingleton':
        """
        Get singleton instance
        
        Args:
            config: Widget configuration object (only used on first call)
            
        Returns:
            TVEngineSingleton: Singleton instance
        """
        if cls._instance is None:
            return cls(config)
        return cls._instance
    
    @classmethod
    def reset(cls) -> None:
        """
        Reset singleton (for testing only)
        
        Warning:
            Do not use in production environment!
        """
        if cls._instance is not None:
            # Deactivate all indicators (if applicable)
            if hasattr(cls._instance, 'deactivate_all'):
                cls._instance.deactivate_all()  # type: ignore
            cls._instance = None
            logger.warning("TVEngine singleton has been reset")

    def setup(self, 
             indicators_dir: Optional[str] = None,
             auto_activate: bool = True,
             config: Optional[Dict[str, Any]] = None) -> 'TVEngineSingleton':

        return self
    
    def run(self, 
            widget_config: Optional[Dict[str, Any]] = None,
            indicators_dir: Optional[str] = None, 
            on_port: int = 0) -> None:
        pass
