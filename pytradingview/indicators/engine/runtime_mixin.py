"""
TVEngine Runtime Functionality
Provides initialization, setup, and runtime entry for the engine
"""

import logging
import json
from typing import Dict, Any, Optional, TYPE_CHECKING

from .drawing_mixin import TVEngineDrawing

if TYPE_CHECKING:
    from ...core.TVWidget import TVWidget
    from ...core.TVChart import TVChart
    from ...core.TVEventBus import Event

logger = logging.getLogger(__name__)


class TVEngineRuntime(TVEngineDrawing):
    """
    Indicator Engine - Runtime Functionality
    
    Provides:
    - Engine initialization
    - Engine setup
    - Engine runtime
    - Widget integration
    - Event handling
    """
    
    def __init__(self, config=None):  # type: ignore
        """
        Initialize indicator engine (only initializes on first call)
        
        Args:
            config: Widget configuration object (optional, will use default configuration)
        """
        # Prevent duplicate initialization
        if hasattr(self, '_initialized') and self._initialized:  # type: ignore
            if config is not None:
                logger.warning(
                    "TVEngine is already initialized. "
                    "Use update_config() to modify configuration."
                )
            return
        
        from ...core.TVWidgetConfig import TVWidgetConfig
        from ...core.TVEventBus import EventBus
        from ..indicator_registry import IndicatorRegistry
        from .chart_context import ChartContextManager
        
        self.registry = IndicatorRegistry.get_instance()
        # Use ChartContextManager to manage multi-chart
        self.chart_context_manager = ChartContextManager()
        self._widget = None
        
        # Configuration management
        self.config = config or TVWidgetConfig()
        
        # Event bus
        self.event_bus = EventBus.get_instance()
        
        # Mark as initialized
        self._initialized = True
        
        logger.info("TVEngine singleton initialized")
    
    def setup(self, 
             indicators_dir: Optional[str] = None,
             auto_activate: bool = True,
             config: Optional[Dict[str, Any]] = None) -> 'TVEngineRuntime':
        """
        Setup indicator engine
        
        Args:
            indicators_dir: Indicator directory path (optional)
            auto_activate: Whether to automatically activate enabled indicators
            config: Widget configuration (optional)
            
        Returns:
            self: Supports method chaining
        """
        # Update configuration
        if config:
            self.config.update(config)  # type: ignore
        
        # Load indicators
        if indicators_dir:
            self.load_indicators_from_directory(indicators_dir)  # type: ignore
        
        # Automatically activate enabled indicators
        if auto_activate:
            enabled_indicators = self.registry.list_enabled()  # type: ignore
            for name in enabled_indicators:
                self.activate_indicator(name)  # type: ignore
        
        return self
    
    def run(self, 
            widget_config: Optional[Dict[str, Any]] = None,
            indicators_dir: Optional[str] = None, 
            on_port: int = 0) -> None:
        """
        Run indicator engine
        
        This is the main entry point for the indicator engine
        
        Args:
            widget_config: TradingView Widget configuration (optional)
            indicators_dir: Indicator directory path (optional)
        """
        from ...core.TVBridge import TVBridge
        from ...core.TVEventBus import EventType
        
        # === 1. Handle configuration ===
        
        # Merge runtime configuration
        if widget_config:
            self.config.update(widget_config)  # type: ignore
        
        # Validate configuration
        if not self.config.validate():  # type: ignore
            raise ValueError("Invalid widget configuration")
        
        logger.info(f"Widget config: {self.config}")  # type: ignore
        
        # === 2. Load indicators ===
        
        if indicators_dir:
            self.load_indicators_from_directory(indicators_dir)  # type: ignore
        
        # === 3. Setup Widget callbacks (register via TVBridge) ===
        
        # Register configuration provider
        TVBridge.get_instance().register_config_provider(self.config)  # type: ignore
        
        # Register chart ready callback
        TVBridge.get_instance().register_chart_ready_callback(self._on_chart_data_ready)
        
        # === 4. Setup event listeners ===
        
        # Listen for chart ready events
        self.event_bus.subscribe(EventType.CHART_READY, self._on_chart_ready_event)  # type: ignore
        
        # === 5. Start Bridge service ===
        
        logger.info("="*60)
        logger.info("Starting Indicator Engine...")
        logger.info(f"Config: {self.config}")  # type: ignore
        logger.info("="*60)
        
        # Publish start event
        self.event_bus.publish_sync(  # type: ignore
            EventType.BRIDGE_STARTED,
            source='TVEngine'
        )
        
        bridge = TVBridge.get_instance()
        bridge.run(on_port=on_port)
    
    async def _on_chart_ready_event(self, event: 'Event') -> None:
        """
        Handle chart ready event
        
        Args:
            event: Chart ready event
        """
        widget = event.data.get('widget')
        if not widget:
            logger.error("No widget in CHART_READY event")
            return
        
        # Execute original logic
        await self._on_chart_data_ready(widget)
    
    async def _on_chart_data_ready(self, widget: 'TVWidget') -> None:
        """
        Chart data ready callback (supports multi-chart)
        
        Initialize all charts and subscribe to layout switch events
        """
        from ...models.TVExportedData import TVExportedData
        
        # Save widget reference
        self._widget = widget
        
        # Subscribe to chart layout switch events
        await self._subscribe_layout_changed_event(widget)
        
        # Initialize all charts in current layout
        await self._initialize_all_charts(widget)
    
    async def _subscribe_layout_changed_event(self, widget: 'TVWidget') -> None:
        """
        Subscribe to chart layout switch events
        
        This event is triggered when the user switches chart layouts (e.g., from 1 chart to 2 charts)
        """
        # Define synchronous wrapper function, internally calling asynchronous logic
        def on_layout_changed_sync(*args):  # type: ignore
            import asyncio
            # Create asynchronous task
            asyncio.create_task(self._handle_layout_changed(widget))
        
        # Subscribe to layout_changed event
        await widget.subscribe('layout_changed', on_layout_changed_sync)  # type: ignore
        logger.info("Subscribed to layout_changed event")
    
    async def _handle_layout_changed(self, widget: 'TVWidget') -> None:
        """
        Handle layout switch event
        """
        logger.info("="*60)
        logger.info("Layout changed detected - Reinitializing charts...")
        logger.info("="*60)
        
        # Clean up old chart contexts
        await self._cleanup_all_charts()
        
        # Reinitialize all charts
        await self._initialize_all_charts(widget)
        
        logger.info("Chart reinitialization completed")
    
    async def _initialize_all_charts(self, widget: 'TVWidget') -> None:
        """
        Initialize all charts
        
        Traverse all charts in the current layout and set up listeners
        """
        # Get chart count
        charts_count = await widget.chartsCount()
        logger.info(f"Initializing {charts_count} chart(s)...")
        
        # Create context and set up event listeners for each chart
        for chart_index in range(charts_count):
            chart_id = f"chart_{chart_index}"
            chart = await widget.chart(chart_index)
            
            # Create chart context
            context = self.chart_context_manager.create_context(chart_id, chart)
            logger.info(f"Created context for {chart_id}")
            
            # Activate default indicators (if configured)
            await self._activate_default_indicators_for_chart(chart_id)
            
            # Set up data loading listener for this chart
            await self._setup_chart_data_listener(widget, chart, chart_id, chart_index)
    
    async def _activate_default_indicators_for_chart(self, chart_id: str) -> None:
        """
        Activate default indicators for new chart
        
        Can decide which indicators to activate based on configuration or enabled status in registry
        """
        # Get enabled indicators
        enabled_indicators = self.registry.list_enabled()  # type: ignore
        
        if not enabled_indicators:
            return
        
        logger.info(f"Activating default indicators for {chart_id}: {enabled_indicators}")
        
        for name in enabled_indicators:
            success = self.activate_indicator(name, chart_id)  # type: ignore
            if success:
                logger.debug(f"Activated '{name}' on {chart_id}")
            else:
                logger.warning(f"Failed to activate '{name}' on {chart_id}")
    
    async def _cleanup_all_charts(self) -> None:
        """
        Clean up all chart contexts and subscriptions
        
        Called before layout switching to ensure old chart resources are properly released
        """
        contexts = self.chart_context_manager.get_all_contexts()  # type: ignore
        
        if not contexts:
            return
        
        logger.info(f"Cleaning up {len(contexts)} chart context(s)...")
        
        # Deactivate all indicators on all charts
        for chart_id in list(contexts.keys()):
            context = self.chart_context_manager.get_context(chart_id)  # type: ignore
            if context:
                # Clean up each indicator
                for name in list(context.get_indicator_names()):
                    indicator = context.get_indicator(name)
                    if indicator:
                        # Clear drawings
                        await indicator.clear_all_drawings()
                        # Call destroy callback
                        indicator.on_destroy()
        
        # Clear all contexts
        self.chart_context_manager.clear_all()  # type: ignore
        logger.info("All chart contexts cleared")
    
    async def _setup_chart_data_listener(self, widget: 'TVWidget', chart: 'TVChart', 
                                         chart_id: str, chart_index: int) -> None:
        """
        Set up data loading listener for a single chart
        
        This method performs two key operations:
        1. Subscribes to future data loading events (onDataLoaded)
        2. Immediately triggers initial indicator calculation for already-loaded data
        
        The immediate trigger is necessary because when chart data is ready,
        the onDataLoaded event may not fire again, so we manually invoke
        the callback to ensure indicators are calculated at least once.
        
        Args:
            widget: TVWidget instance
            chart: TVChart instance
            chart_id: Unique chart identifier
            chart_index: Chart index in the layout
        """
        from ...models.TVExportedData import TVExportedData
        
        async def on_data_loaded_callback(**kwargs):  # type: ignore
            logger.info(f"Data loaded for {chart_id} (index={chart_index})")
            
            # Get chart context
            context = self.chart_context_manager.get_context(chart_id)
            if not context:
                logger.error(f"Context not found for {chart_id}")
                return
            
            # Initialize all active indicators on this chart
            for name, indicator in context.active_indicators.items():
                indicator.on_init(widget, chart, chart_id)
                logger.debug(f"Initialized indicator '{name}' on {chart_id}")
            
            async def export_callback(**export_kwargs):  # type: ignore
                exported_data_dict = export_kwargs.get("exportedData") or {}
                data_model = TVExportedData().from_json(json_data=exported_data_dict)
                df = data_model.to_dataframe()
                
                if df.empty:
                    logger.error(f"Exported data is empty for {chart_id}")
                    return
                
                # Run indicators on this chart
                results = await self.run_indicators_for_chart(chart_id, df)  # type: ignore
                
                # Print result summary
                for name, result in results.items():
                    if result['success']:
                        logger.info(
                            f"[{chart_id}] Indicator '{name}': "
                            f"{len(result['signals'])} signals, "
                            f"{len(result['drawables'])} drawables"
                        )
                    else:
                        logger.error(f"[{chart_id}] Indicator '{name}' failed: {result['error']}")
            
            await chart.exportData(callback=export_callback)
        
        # Subscribe to future data loading events
        subscription = await chart.onDataLoaded()
        await subscription.subscribe(callback=on_data_loaded_callback)
        
        # Trigger initial indicator calculation immediately
        # This is crucial: when _handle_chart_data_ready is called, the chart data
        # is already loaded, but onDataLoaded event won't fire again. We must
        # manually trigger the callback once to calculate indicators on existing data.
        logger.debug(f"Triggering initial indicator calculation for {chart_id}")
        await on_data_loaded_callback()
