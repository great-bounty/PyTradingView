"""
Indicator Registry - Manage Registered Indicators
"""

from typing import Dict, List, Type, Optional, Any
import logging

from .indicator_base import TVIndicator

logger = logging.getLogger(__name__)


class IndicatorRegistry:
    """
    Indicator Registry
    
    Responsible for managing all registered indicator classes
    Uses singleton pattern to ensure global uniqueness
    """
    
    _instance: Optional['IndicatorRegistry'] = None
    
    def __init__(self):
        """Initialize registry"""
        if IndicatorRegistry._instance is not None:
            raise RuntimeError("IndicatorRegistry is a singleton. Use get_instance() instead.")
        
        self._indicators: Dict[str, Type[TVIndicator]] = {}
        self._enabled_indicators: Dict[str, bool] = {}
    
    @classmethod
    def get_instance(cls) -> 'IndicatorRegistry':
        """Get registry singleton"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @classmethod
    def reset(cls) -> None:
        """Reset registry (mainly for testing)"""
        cls._instance = None
    
    def register(self, 
                 indicator_class: Type[TVIndicator], 
                 name: Optional[str] = None,
                 enabled: bool = True) -> None:
        """
        Register indicator
        
        Args:
            indicator_class: Indicator class (must inherit from TVIndicator)
            name: Indicator name (optional, defaults to class name)
            enabled: Whether to enable
            
        Raises:
            TypeError: If indicator class is not a subclass of TVIndicator
            ValueError: If indicator name already exists
        """
        # Validate type
        if not issubclass(indicator_class, TVIndicator):
            raise TypeError(
                f"Indicator class {indicator_class.__name__} must inherit from TVIndicator"
            )
        
        # Determine indicator name
        indicator_name = name or indicator_class.__name__
        
        # Check if already registered
        if indicator_name in self._indicators:
            logger.warning(f"Indicator '{indicator_name}' is already registered. Overwriting...")
        
        # Register indicator
        self._indicators[indicator_name] = indicator_class
        self._enabled_indicators[indicator_name] = enabled
        
        logger.info(f"Registered indicator: {indicator_name} (enabled={enabled})")
    
    def unregister(self, name: str) -> bool:
        """
        Unregister indicator
        
        Args:
            name: Indicator name
            
        Returns:
            bool: Whether unregistration was successful
        """
        if name in self._indicators:
            del self._indicators[name]
            del self._enabled_indicators[name]
            logger.info(f"Unregistered indicator: {name}")
            return True
        else:
            logger.warning(f"Indicator '{name}' not found in registry")
            return False
    
    def get(self, name: str) -> Optional[Type[TVIndicator]]:
        """
        Get indicator class
        
        Args:
            name: Indicator name
            
        Returns:
            Indicator class, or None if not found
        """
        return self._indicators.get(name)
    
    def create_instance(self, name: str) -> Optional[TVIndicator]:
        """
        Create indicator instance
        
        Args:
            name: Indicator name
            
        Returns:
            Indicator instance, or None if not found
        """
        indicator_class = self.get(name)
        if indicator_class is None:
            logger.error(f"Indicator '{name}' not found in registry")
            return None
        
        try:
            instance = indicator_class()
            logger.debug(f"Created instance of indicator: {name}")
            return instance
        except Exception as e:
            logger.error(f"Failed to create instance of indicator '{name}': {e}")
            return None
    
    def is_registered(self, name: str) -> bool:
        """
        Check if indicator is registered
        
        Args:
            name: Indicator name
            
        Returns:
            bool: Whether registered
        """
        return name in self._indicators
    
    def is_enabled(self, name: str) -> bool:
        """
        Check if indicator is enabled
        
        Args:
            name: Indicator name
            
        Returns:
            bool: Whether enabled
        """
        return self._enabled_indicators.get(name, False)
    
    def enable(self, name: str) -> bool:
        """
        Enable indicator
        
        Args:
            name: Indicator name
            
        Returns:
            bool: Whether enabling was successful
        """
        if name in self._indicators:
            self._enabled_indicators[name] = True
            logger.info(f"Enabled indicator: {name}")
            return True
        else:
            logger.warning(f"Indicator '{name}' not found in registry")
            return False
    
    def disable(self, name: str) -> bool:
        """
        Disable indicator
        
        Args:
            name: Indicator name
            
        Returns:
            bool: Whether disabling was successful
        """
        if name in self._indicators:
            self._enabled_indicators[name] = False
            logger.info(f"Disabled indicator: {name}")
            return True
        else:
            logger.warning(f"Indicator '{name}' not found in registry")
            return False
    
    def list_all(self) -> List[str]:
        """
        List all registered indicator names
        
        Returns:
            List of indicator names
        """
        return list(self._indicators.keys())
    
    def list_enabled(self) -> List[str]:
        """
        List all enabled indicators names
        
        Returns:
            List of enabled indicators names
        """
        return [name for name, enabled in self._enabled_indicators.items() if enabled]
    
    def clear(self) -> None:
        """Clear registry"""
        self._indicators.clear()
        self._enabled_indicators.clear()
        logger.info("Cleared indicator registry")
    
    def get_info(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all indicators info
        
        Returns:
            Indicators info dictionary
        """
        info = {}
        for name, indicator_class in self._indicators.items():
            try:
                # Create temporary instance to get config
                temp_instance = indicator_class()
                config = temp_instance.get_config()
                
                info[name] = {
                    'class': indicator_class.__name__,
                    'enabled': self._enabled_indicators[name],
                    'config': config.to_dict() if config else {}
                }
            except Exception as e:
                logger.error(f"Failed to get info for indicator '{name}': {e}")
                info[name] = {
                    'class': indicator_class.__name__,
                    'enabled': self._enabled_indicators[name],
                    'error': str(e)
                }
        
        return info


# Decorator: used for auto registering indicators
def register_indicator(name: Optional[str] = None, enabled: bool = True):
    """
    Indicator registration decorator
    
    Usage:
        @register_indicator(name="MyIndicator", enabled=True)
        class MyIndicator(TVIndicator):
            ...
    
    Args:
        name: Indicator name (optional)
        enabled: Whether to enable
    """
    def decorator(indicator_class: Type[TVIndicator]):
        registry = IndicatorRegistry.get_instance()
        registry.register(indicator_class, name=name, enabled=enabled)
        return indicator_class
    
    return decorator
