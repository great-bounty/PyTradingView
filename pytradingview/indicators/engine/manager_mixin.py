"""
TVEngine Indicator Management Functionality
Provides activation, deactivation, and lifecycle management of indicators (supports multi-chart)
"""

import logging
from typing import Dict, Optional, List, TYPE_CHECKING

from .loader_mixin import TVEngineLoader
from ..indicator_base import TVIndicator
from ..indicator_registry import IndicatorRegistry
from .chart_context import ChartContextManager, ChartContext

if TYPE_CHECKING:
    from ...core.TVWidget import TVWidget
    from ...core.TVChart import TVChart

logger = logging.getLogger(__name__)


class TVEngineManager(TVEngineLoader):
    """
    Indicator Engine - Indicator Management Functionality
    
    Provides:
    - Activate/deactivate indicators
    - Manage active indicator collections
    - Indicator lifecycle management
    """
    
    def __init__(self, config=None):  # type: ignore
        """Initialize indicator manager"""
        # Do not call super().__init__(), unified initialization by final class
        
        if not hasattr(self, '_initialized') or not self._initialized:  # type: ignore
            self.registry = IndicatorRegistry.get_instance()
            # Deprecated active_indicators, now using ChartContextManager
            self.chart_context_manager = ChartContextManager()
            self._widget: Optional['TVWidget'] = None
    
    def activate_indicator(self, name: str, chart_id: Optional[str] = None) -> bool:
        """
        Activate indicator
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional, if not specified activate to all charts)
            
        Returns:
            bool: Whether activation was successful
        """
        if chart_id is not None:
            # Activate to specified chart
            return self._activate_indicator_to_chart(name, chart_id)
        else:
            # Activate to all charts
            return self._activate_indicator_to_all_charts(name)
    
    def _activate_indicator_to_chart(self, name: str, chart_id: str) -> bool:
        """Activate indicator to specified chart"""
        context = self.chart_context_manager.get_context(chart_id)
        if not context:
            logger.warning(f"Chart context '{chart_id}' not found")
            return False
        
        if context.has_indicator(name):
            logger.warning(f"Indicator '{name}' is already active on chart '{chart_id}'")
            return True
        
        # Create indicator instance
        indicator = self.registry.create_instance(name)
        if indicator is None:
            return False
        
        # Set chart_id
        indicator.set_chart_id(chart_id)
        
        # If widget and chart already exist, initialize immediately
        if self._widget and context.chart:
            indicator.on_init(self._widget, context.chart, chart_id)
        
        context.add_indicator(name, indicator)
        logger.info(f"Activated indicator '{name}' on chart '{chart_id}'")
        return True
    
    def _activate_indicator_to_all_charts(self, name: str) -> bool:
        """Activate indicator to all charts"""
        contexts = self.chart_context_manager.get_all_contexts()
        if not contexts:
            logger.warning("No chart contexts available")
            return False
        
        success = True
        for chart_id in contexts.keys():
            if not self._activate_indicator_to_chart(name, chart_id):
                success = False
        
        return success
    
    def deactivate_indicator(self, name: str, chart_id: Optional[str] = None) -> bool:
        """
        Deactivate indicator
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional, if not specified deactivate from all charts)
            
        Returns:
            bool: Whether deactivation was successful
        """
        if chart_id is not None:
            # Deactivate from specified chart
            return self._deactivate_indicator_from_chart(name, chart_id)
        else:
            # Deactivate from all charts
            return self._deactivate_indicator_from_all_charts(name)
    
    def _deactivate_indicator_from_chart(self, name: str, chart_id: str) -> bool:
        """Deactivate indicator from specified chart"""
        context = self.chart_context_manager.get_context(chart_id)
        if not context:
            logger.warning(f"Chart context '{chart_id}' not found")
            return False
        
        if not context.has_indicator(name):
            logger.warning(f"Indicator '{name}' is not active on chart '{chart_id}'")
            return False
        
        # Call destroy callback
        indicator = context.get_indicator(name)
        if indicator:
            indicator.on_destroy()
        
        # Remove
        context.remove_indicator(name)
        logger.info(f"Deactivated indicator '{name}' from chart '{chart_id}'")
        return True
    
    def _deactivate_indicator_from_all_charts(self, name: str) -> bool:
        """Deactivate indicator from all charts"""
        contexts = self.chart_context_manager.get_all_contexts()
        if not contexts:
            return False
        
        success = True
        for chart_id in contexts.keys():
            if not self._deactivate_indicator_from_chart(name, chart_id):
                success = False
        
        return success
    
    def deactivate_all(self, chart_id: Optional[str] = None) -> None:
        """
        Deactivate all indicators
        
        Args:
            chart_id: Chart ID (optional, if not specified deactivate all indicators from all charts)
        """
        if chart_id is not None:
            context = self.chart_context_manager.get_context(chart_id)
            if context:
                for name in list(context.get_indicator_names()):
                    self._deactivate_indicator_from_chart(name, chart_id)
        else:
            # Deactivate all indicators from all charts
            for context in self.chart_context_manager.get_all_contexts().values():
                for name in list(context.get_indicator_names()):
                    self._deactivate_indicator_from_chart(name, context.chart_id)
    
    def get_active_indicators(self, chart_id: Optional[str] = None) -> Dict[str, TVIndicator]:
        """
        Get active indicator dictionary
        
        Args:
            chart_id: Chart ID (optional, if not specified return indicators from first chart)
            
        Returns:
            Indicator dictionary
        """
        if chart_id is not None:
            context = self.chart_context_manager.get_context(chart_id)
            return context.active_indicators if context else {}
        else:
            # Return indicators from first chart (backward compatible)
            contexts = self.chart_context_manager.get_all_contexts()
            if contexts:
                first_context = next(iter(contexts.values()))
                return first_context.active_indicators
            return {}
    
    def get_all_chart_indicators(self) -> Dict[str, Dict[str, TVIndicator]]:
        """
        Get indicators from all charts
        
        Returns:
            {chart_id: {indicator_name: indicator_instance}}
        """
        result = {}
        for chart_id, context in self.chart_context_manager.get_all_contexts().items():
            result[chart_id] = context.active_indicators.copy()
        return result
