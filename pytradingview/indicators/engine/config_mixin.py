"""
TVEngine Configuration Management Functionality
Provide dynamic configuration updates and indicator parameter management
"""

import logging
from typing import Dict, Any, List, Tuple, Optional

from .manager_mixin import TVEngineManager

logger = logging.getLogger(__name__)


class TVEngineConfig(TVEngineManager):
    """
    Indicator Engine - Configuration Management Functionality
    
    Provides:
    - Engine configuration management
    - Indicator configuration management
    - Indicator parameter updates
    - Indicator style updates
    - Indicator recalculation
    """
    
    def __init__(self, config=None):  # type: ignore
        """Initialize configuration manager"""
        # Do not call super().__init__(), unified initialization by final class
        
        if not hasattr(self, '_initialized') or not self._initialized:  # type: ignore
            from ...core.TVWidgetConfig import TVWidgetConfig
            from ...core.TVEventBus import EventBus
            
            # Configuration management
            self.config = config or TVWidgetConfig()
            
            # Event bus
            self.event_bus = EventBus.get_instance()
    
    # === Engine Configuration Management ===
    
    def update_config(self, config_dict: Dict[str, Any]) -> 'TVEngineConfig':
        """
        Update engine configuration
        
        Args:
            config_dict: Configuration dictionary
            
        Returns:
            self: Support for chaining calls
        """
        self.config.update(config_dict)
        logger.info(f"Engine config updated: {config_dict}")
        return self
    
    def get_config(self) -> Dict[str, Any]:
        """
        Get current configuration
        
        Returns:
            Dict: Configuration dictionary
        """
        return self.config.to_dict()
    
    def set_config(self, config: Dict[str, Any]) -> 'TVEngineConfig':
        """
        Set Widget configuration
        
        Args:
            config: Configuration dictionary
            
        Returns:
            self: Support for chaining calls
        """
        self.config.update(config)
        return self
    
    # === Indicator Configuration Management ===
    
    def get_indicator_config(self, name: str, chart_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get indicator configuration
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional, if not specified, get from first chart)
            
        Returns:
            Configuration dictionary, or None if indicator does not exist
        """
        context = self._get_chart_context(chart_id)  # type: ignore
        if not context:
            logger.warning(f"Chart context not found")
            return None
        
        if not context.has_indicator(name):
            logger.warning(f"Indicator '{name}' is not active on chart '{context.chart_id}'")
            return None
        
        indicator = context.get_indicator(name)
        return indicator.get_config_dict() if indicator else None
    
    def update_indicator_config(self, name: str, config_dict: Dict[str, Any], 
                               chart_id: Optional[str] = None) -> Tuple[bool, List[str]]:
        """
        Update indicator configuration
        
        Args:
            name: Indicator name
            config_dict: Configuration dictionary
            chart_id: Chart ID (optional, if not specified, update the indicator on all charts)
            
        Returns:
            (success, errors): Whether successful, list of error messages
        """
        if chart_id is not None:
            return self._update_indicator_config_for_chart(name, config_dict, chart_id)
        else:
            # Update the indicator on all charts
            all_errors = []
            success = True
            for cid in self.chart_context_manager.get_chart_ids():  # type: ignore
                result, errors = self._update_indicator_config_for_chart(name, config_dict, cid)
                if not result:
                    success = False
                    all_errors.extend(errors)
            return success, all_errors
    
    def _update_indicator_config_for_chart(self, name: str, config_dict: Dict[str, Any],
                                          chart_id: str) -> Tuple[bool, List[str]]:
        """Update indicator configuration on specified chart"""
        context = self.chart_context_manager.get_context(chart_id)  # type: ignore
        if not context:
            return False, [f"Chart context '{chart_id}' not found"]
        
        if not context.has_indicator(name):
            return False, [f"Indicator '{name}' is not active on chart '{chart_id}'"]
        
        indicator = context.get_indicator(name)
        if indicator:
            return indicator.update_config(config_dict)
        return False, ["Indicator instance is None"]
    
    def update_indicator_input(self, name: str, input_id: str, value: Any,
                              chart_id: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        """
        Update indicator input parameter
        
        Args:
            name: Indicator name
            input_id: Parameter ID
            value: New value
            chart_id: Chart ID (optional)
            
        Returns:
            (success, error): Whether successful, error message
        """
        context = self._get_chart_context(chart_id)  # type: ignore
        if not context:
            return False, "Chart context not found"
        
        if not context.has_indicator(name):
            return False, f"Indicator '{name}' is not active on chart '{context.chart_id}'"
        
        indicator = context.get_indicator(name)
        return indicator.update_input_value(input_id, value) if indicator else (False, "Indicator instance is None")
    
    def update_indicator_style(self, name: str, style_id: str, chart_id: Optional[str] = None,
                              **kwargs) -> Tuple[bool, Optional[str]]:
        """
        Update indicator style
        
        Args:
            name: Indicator name
            style_id: Style ID
            chart_id: Chart ID (optional)
            **kwargs: Style properties
            
        Returns:
            (success, error): Whether successful, error message
        """
        context = self._get_chart_context(chart_id)  # type: ignore
        if not context:
            return False, "Chart context not found"
        
        if not context.has_indicator(name):
            return False, f"Indicator '{name}' is not active on chart '{context.chart_id}'"
        
        indicator = context.get_indicator(name)
        return indicator.update_style(style_id, **kwargs) if indicator else (False, "Indicator instance is None")
    
    async def recalculate_indicator(self, name: str, chart_id: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        """
        Recalculate indicator
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional)
            
        Returns:
            (success, error): Whether successful, error message
        """
        context = self._get_chart_context(chart_id)  # type: ignore
        if not context:
            return False, "Chart context not found"
        
        if not context.has_indicator(name):
            return False, f"Indicator '{name}' is not active on chart '{context.chart_id}'"
        
        indicator = context.get_indicator(name)
        return await indicator.recalculate_and_redraw() if indicator else (False, "Indicator instance is None")
    
    async def recalculate_all_indicators(self, chart_id: Optional[str] = None) -> Dict[str, Tuple[bool, Optional[str]]]:
        """
        Recalculate all indicators
        
        Args:
            chart_id: Chart ID (optional, if not specified, recalculate all indicators on all charts)
        
        Returns:
            Results dictionary for each indicator
        """
        results = {}
        
        if chart_id is not None:
            context = self.chart_context_manager.get_context(chart_id)  # type: ignore
            if context:
                for name in context.get_indicator_names():
                    results[f"{chart_id}:{name}"] = await self.recalculate_indicator(name, chart_id)
        else:
            # Recalculate all indicators on all charts
            for cid, context in self.chart_context_manager.get_all_contexts().items():  # type: ignore
                for name in context.get_indicator_names():
                    results[f"{cid}:{name}"] = await self.recalculate_indicator(name, cid)
        
        return results
    
    def get_all_configs(self, chart_id: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
        """
        Get configurations of all active indicators
        
        Args:
            chart_id: Chart ID (optional, if not specified, return indicator configurations for all charts)
        
        Returns:
            Mapping from indicator name to configuration
        """
        configs = {}
        
        if chart_id is not None:
            context = self.chart_context_manager.get_context(chart_id)  # type: ignore
            if context:
                for name, indicator in context.active_indicators.items():
                    configs[f"{chart_id}:{name}"] = indicator.get_config_dict()
        else:
            # Return all indicator configurations for all charts
            for cid, context in self.chart_context_manager.get_all_contexts().items():  # type: ignore
                for name, indicator in context.active_indicators.items():
                    configs[f"{cid}:{name}"] = indicator.get_config_dict()
        
        return configs
    
    def _get_chart_context(self, chart_id: Optional[str]):
        """Get chart context (return first if not specified)"""
        if chart_id is not None:
            return self.chart_context_manager.get_context(chart_id)  # type: ignore
        else:
            # Return first chart context (backward compatibility)
            contexts = self.chart_context_manager.get_all_contexts()  # type: ignore
            if contexts:
                return next(iter(contexts.values()))
            return None
