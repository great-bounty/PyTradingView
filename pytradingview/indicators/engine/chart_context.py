"""
Chart Context - Manage indicator instances and state for individual charts

Provide data isolation for multi-chart scenarios, each chart maintains independent:
- Indicator instance collection
- Drawing object references
- Chart state cache
"""

from typing import Dict, Optional, TYPE_CHECKING
from dataclasses import dataclass, field
import logging

if TYPE_CHECKING:
    from ...core.TVChart import TVChart
    from ..indicator_base import TVIndicator

logger = logging.getLogger(__name__)


@dataclass
class ChartContext:
    """
    Chart Context Data Class
    
    Each chart instance corresponds to a ChartContext, including:
    - chart_id: Unique chart identifier
    - chart: TVChart instance reference
    - active_indicators: Dictionary of active indicator instances
    - symbol: Current trading instrument
    - interval: Current time period
    """
    
    chart_id: str
    chart: 'TVChart'
    active_indicators: Dict[str, 'TVIndicator'] = field(default_factory=dict)
    symbol: Optional[str] = None
    interval: Optional[str] = None
    
    def __post_init__(self):
        """Post-initialization processing"""
        logger.info(f"Created ChartContext for chart_id={self.chart_id}")
    
    def add_indicator(self, name: str, indicator: 'TVIndicator') -> None:
        """
        Add indicator to this chart context
        
        Args:
            name: Indicator name
            indicator: Indicator instance
        """
        self.active_indicators[name] = indicator
        logger.debug(f"Chart {self.chart_id}: Added indicator '{name}'")
    
    def remove_indicator(self, name: str) -> Optional['TVIndicator']:
        """
        Remove indicator from this chart context
        
        Args:
            name: Indicator name
            
        Returns:
            Removed indicator instance, or None if not exists
        """
        indicator = self.active_indicators.pop(name, None)
        if indicator:
            logger.debug(f"Chart {self.chart_id}: Removed indicator '{name}'")
        return indicator
    
    def get_indicator(self, name: str) -> Optional['TVIndicator']:
        """
        Get indicator instance
        
        Args:
            name: Indicator name
            
        Returns:
            Indicator instance, or None if not exists
        """
        return self.active_indicators.get(name)
    
    def has_indicator(self, name: str) -> bool:
        """
        Check if specified indicator exists
        
        Args:
            name: Indicator name
            
        Returns:
            Whether it exists
        """
        return name in self.active_indicators
    
    def clear_all_indicators(self) -> None:
        """Clear all indicators"""
        count = len(self.active_indicators)
        self.active_indicators.clear()
        logger.info(f"Chart {self.chart_id}: Cleared {count} indicators")
    
    def get_indicator_names(self) -> list[str]:
        """Get list of all active indicator names"""
        return list(self.active_indicators.keys())
    
    def update_symbol_interval(self, symbol: Optional[str] = None, interval: Optional[str] = None) -> None:
        """
        Update chart's symbol and interval information
        
        Args:
            symbol: Trading instrument
            interval: Time period
        """
        if symbol is not None:
            self.symbol = symbol
        if interval is not None:
            self.interval = interval
        logger.debug(f"Chart {self.chart_id}: Updated to {self.symbol}/{self.interval}")


class ChartContextManager:
    """
    Chart Context Manager
    
    Manage contexts for all charts, providing:
    - Creation and destruction of chart contexts
    - Cross-chart query operations
    - Global indicator management
    """
    
    def __init__(self):
        """Initialize chart context manager"""
        self._contexts: Dict[str, ChartContext] = {}
        logger.info("ChartContextManager initialized")
    
    def create_context(self, chart_id: str, chart: 'TVChart') -> ChartContext:
        """
        Create new chart context
        
        Args:
            chart_id: Chart ID
            chart: TVChart instance
            
        Returns:
            Newly created chart context
        """
        if chart_id in self._contexts:
            logger.warning(f"ChartContext for {chart_id} already exists, will be replaced")
        
        context = ChartContext(chart_id=chart_id, chart=chart)
        self._contexts[chart_id] = context
        return context
    
    def get_context(self, chart_id: str) -> Optional[ChartContext]:
        """
        Get context for specified chart
        
        Args:
            chart_id: Chart ID
            
        Returns:
            Chart context, or None if not exists
        """
        return self._contexts.get(chart_id)
    
    def remove_context(self, chart_id: str) -> Optional[ChartContext]:
        """
        Remove chart context
        
        Args:
            chart_id: Chart ID
            
        Returns:
            Removed chart context, or None if not exists
        """
        context = self._contexts.pop(chart_id, None)
        if context:
            logger.info(f"Removed ChartContext for {chart_id}")
        return context
    
    def get_all_contexts(self) -> Dict[str, ChartContext]:
        """Get all chart contexts"""
        return self._contexts.copy()
    
    def get_chart_ids(self) -> list[str]:
        """Get list of all chart IDs"""
        return list(self._contexts.keys())
    
    def clear_all(self) -> None:
        """Clear all chart contexts"""
        count = len(self._contexts)
        self._contexts.clear()
        logger.info(f"Cleared all {count} chart contexts")
    
    def has_context(self, chart_id: str) -> bool:
        """
        Check if context exists for specified chart
        
        Args:
            chart_id: Chart ID
            
        Returns:
            Whether it exists
        """
        return chart_id in self._contexts
    
    def get_charts_with_indicator(self, indicator_name: str) -> list[str]:
        """
        Get list of chart IDs that have activated the specified indicator
        
        Args:
            indicator_name: Indicator name
            
        Returns:
            List of chart IDs
        """
        return [
            chart_id for chart_id, context in self._contexts.items()
            if context.has_indicator(indicator_name)
        ]
    
    def count_total_indicators(self) -> int:
        """Count total number of indicators across all charts"""
        return sum(len(ctx.active_indicators) for ctx in self._contexts.values())
