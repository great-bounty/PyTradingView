"""
TradingView Widget Configuration Manager

Responsibilities:
- Manage Widget initialization configuration
- Provide configuration validation and default values
- Support configuration inheritance and merging
"""

from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class TVWidgetConfig:
    """
    TradingView Widget Configuration Manager
    
    Provides type-safe configuration management, avoiding the use of global variables
    """
    
    # Default configuration
    DEFAULT_CONFIG: Dict[str, Any] = {
        "symbol": "BTCUSDT",
        "interval": "1D",
        "theme": "Dark",
        "locale": "zh",
        "fullScreen": True,
        "debug": False,
        "autosize": True,
        "timezone": "Asia/Shanghai"
    }
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize configuration manager
        
        Args:
            config: User-provided configuration dictionary
        """
        self._config: Dict[str, Any] = {}
        
        # Load default configuration
        self._config.update(self.DEFAULT_CONFIG)
        
        # Merge user configuration
        if config:
            self.update(config)
    
    def update(self, config: Dict[str, Any]) -> None:
        """
        Update configuration
        
        Args:
            config: Configuration items to update
        """
        if not isinstance(config, dict):
            logger.warning(f"Invalid config type: {type(config)}, expected dict")
            return
        
        self._config.update(config)
        logger.debug(f"Config updated: {list(config.keys())}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration item
        
        Args:
            key: Configuration key name
            default: Default value
            
        Returns:
            Configuration value
        """
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a single configuration item
        
        Args:
            key: Configuration key name
            value: Configuration value
        """
        self._config[key] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Export as dictionary
        
        Returns:
            A copy of the configuration dictionary
        """
        return self._config.copy()
    
    def validate(self) -> bool:
        """
        Validate the validity of the configuration
        
        Returns:
            Whether the configuration is valid
        """
        required_fields = ["symbol", "interval"]
        
        for field in required_fields:
            if field not in self._config:
                logger.error(f"Missing required config field: {field}")
                return False
        
        return True
    
    def __repr__(self) -> str:
        return f"TVWidgetConfig({self._config})"
