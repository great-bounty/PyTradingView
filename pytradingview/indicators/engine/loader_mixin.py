"""
TVEngine Module Loading Functionality
Provides the ability to dynamically load indicators from files and directories
"""

import os
import sys
import importlib
import importlib.util
from pathlib import Path
import logging
from typing import Optional

from .singleton_mixin import TVEngineSingleton
from ..indicator_base import TVIndicator
from ..indicator_registry import IndicatorRegistry

logger = logging.getLogger(__name__)


class TVEngineLoader(TVEngineSingleton):
    """
    Indicator Engine - Module Loading Functionality
    
    Provides:
    - Loading indicators from files
    - Loading indicators from directories (supports recursive)
    - Automatic discovery and registration of indicator classes
    """
    
    def load_indicator_from_file(self, file_path: str) -> bool:
        """
        Load indicator module from file
        
        Args:
            file_path: Indicator file path
            
        Returns:
            bool: Whether loading was successful
        """
        try:
            # Verify file exists
            if not os.path.exists(file_path):
                logger.error(f"Indicator file not found: {file_path}")
                return False
            
            # Get module name
            module_name = Path(file_path).stem
            
            # Load module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                logger.error(f"Failed to load spec from {file_path}")
                return False
            
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            
            # Find TVIndicator subclasses
            indicator_classes = []
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, TVIndicator) and 
                    attr is not TVIndicator):
                    indicator_classes.append(attr)
            
            if not indicator_classes:
                logger.warning(f"No indicator class found in {file_path}")
                return False
            
            # Register all found indicator classes
            registry = IndicatorRegistry.get_instance()
            for indicator_class in indicator_classes:
                # Check if already registered via decorator
                # If class name or other name already exists in registry, skip auto-registration
                class_name = indicator_class.__name__
                already_registered = False
                
                # Check if already registered by class name
                if registry.is_registered(class_name):
                    registered_class = registry.get(class_name)
                    if registered_class is indicator_class:
                        logger.debug(f"Indicator '{class_name}' already registered, skipping auto-registration")
                        already_registered = True
                
                # Check if registered under another name (via decorator)
                if not already_registered:
                    for reg_name in registry.list_all():
                        if registry.get(reg_name) is indicator_class:
                            logger.debug(f"Indicator class '{class_name}' already registered as '{reg_name}', skipping auto-registration")
                            already_registered = True
                            break
                
                # If not registered, then register
                if not already_registered:
                    # Try to get enabled status from indicator config
                    enabled = True  # Default enabled
                    try:
                        temp_instance = indicator_class()
                        config = temp_instance.get_config()
                        if config and hasattr(config, 'enabled'):
                            enabled = config.enabled
                            logger.debug(f"Using enabled={enabled} from indicator config")
                    except Exception as e:
                        logger.debug(f"Could not read config from {class_name}, using default enabled=True: {e}")
                    
                    registry.register(indicator_class, enabled=enabled)
                    logger.info(f"Loaded indicator: {indicator_class.__name__} from {file_path} (enabled={enabled})")
                else:
                    logger.info(f"Indicator {indicator_class.__name__} from {file_path} was already registered (possibly via decorator)")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to load indicator from {file_path}: {e}", exc_info=True)
            return False
    
    def load_indicators_from_directory(self, directory: str, recursive: bool = False) -> int:
        """
        Load all indicator modules from directory
        
        Args:
            directory: Indicator directory path
            recursive: Whether to recursively search subdirectories
            
        Returns:
            int: Number of successfully loaded indicators
        """
        if not os.path.isdir(directory):
            logger.error(f"Directory not found: {directory}")
            return 0
        
        loaded_count = 0
        pattern = "**/*.py" if recursive else "*.py"
        
        for file_path in Path(directory).glob(pattern):
            # Skip __init__.py and __pycache__
            if file_path.name.startswith('__'):
                continue
            
            if self.load_indicator_from_file(str(file_path)):
                loaded_count += 1
        
        logger.info(f"Loaded {loaded_count} indicators from {directory}")
        return loaded_count
