"""
TVEngine Remote Call Functionality
Provides remote call interfaces for Electron IPC
"""

import logging
from typing import Dict, Any, Tuple, Optional

from .config_mixin import TVEngineConfig
from ..indicator_registry import IndicatorRegistry

logger = logging.getLogger(__name__)


class TVEngineRemote(TVEngineConfig):
    """
    Indicator Engine - Remote Call Functionality
    
    Provides:
    - Get engine status
    - Remote update configuration
    - Remote load indicators
    - Remote activate/deactivate indicators
    - Remote update indicator configurations
    - Remote recalculate indicators
    - Get indicator information
    """
    
    def remote_get_status(self, chart_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get engine status (remote call)
        
        Args:
            chart_id: Chart ID (optional, if not specified return global status)
        
        Returns:
            Dict: Engine status information
        """
        registry = IndicatorRegistry.get_instance()
        
        # Basic information
        status = {
            'initialized': self._initialized if hasattr(self, '_initialized') else False,  # type: ignore
            'config': self.config.to_dict() if hasattr(self, 'config') else {},  # type: ignore
            'all_indicators': registry.list_all(),
            'enabled_indicators': registry.list_enabled(),
            'widget_connected': self._widget is not None if hasattr(self, '_widget') else False,  # type: ignore
        }
        
        # Chart information
        if hasattr(self, 'chart_context_manager'):
            contexts = self.chart_context_manager.get_all_contexts()  # type: ignore
            status['chart_count'] = len(contexts)
            status['chart_ids'] = list(contexts.keys())
            
            if chart_id is not None:
                # Return status of specified chart
                context = self.chart_context_manager.get_context(chart_id)  # type: ignore
                if context:
                    status['chart_id'] = chart_id
                    status['active_indicators'] = context.get_indicator_names()
                    status['symbol'] = context.symbol
                    status['interval'] = context.interval
                else:
                    status['error'] = f"Chart '{chart_id}' not found"
            else:
                # Return all charts indicators
                chart_indicators = {}
                for cid, ctx in contexts.items():
                    chart_indicators[cid] = {
                        'indicators': ctx.get_indicator_names(),
                        'symbol': ctx.symbol,
                        'interval': ctx.interval
                    }
                status['charts'] = chart_indicators
        else:
            # Backward compatibility
            status['active_indicators'] = list(self.active_indicators.keys()) if hasattr(self, 'active_indicators') else []  # type: ignore
            status['chart_connected'] = self._chart is not None if hasattr(self, '_chart') else False  # type: ignore
        
        return status
    
    def remote_update_config(self, config_dict: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Remote update configuration
        
        Args:
            config_dict: Configuration dictionary
            
        Returns:
            (success, error): Whether successful, error message
        """
        try:
            self.update_config(config_dict)
            return True, None
        except Exception as e:
            error_msg = f"Failed to update config: {str(e)}"
            logger.error(error_msg)
            return False, error_msg
    
    def remote_load_indicator(self, file_path: str) -> Tuple[bool, Optional[str]]:
        """
        Remote load indicator
        
        Args:
            file_path: Indicator file path
            
        Returns:
            (success, error): Whether successful, error message
        """
        try:
            success = self.load_indicator_from_file(file_path)  # type: ignore
            if success:
                return True, None
            else:
                return False, f"Failed to load indicator from {file_path}"
        except Exception as e:
            error_msg = f"Exception while loading indicator: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg
    
    def remote_activate_indicator(self, name: str, chart_id: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        """
        Remote activate indicator
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional, if not specified activate to all charts)
            
        Returns:
            (success, error): Whether successful, error message
        """
        try:
            success = self.activate_indicator(name, chart_id)  # type: ignore
            if success:
                return True, None
            else:
                return False, f"Failed to activate indicator '{name}'"
        except Exception as e:
            error_msg = f"Exception while activating indicator: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg
    
    def remote_deactivate_indicator(self, name: str, chart_id: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        """
        Remote deactivate indicator
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional, if not specified deactivate from all charts)
            
        Returns:
            (success, error): Whether successful, error message
        """
        try:
            success = self.deactivate_indicator(name, chart_id)  # type: ignore
            if success:
                return True, None
            else:
                return False, f"Failed to deactivate indicator '{name}'"
        except Exception as e:
            error_msg = f"Exception while deactivating indicator: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg
    
    def remote_update_indicator_config(self, name: str, config_dict: Dict[str, Any],
                                      chart_id: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        """
        Remote update indicator configuration
        
        Args:
            name: Indicator name
            config_dict: Configuration dictionary
            chart_id: Chart ID (optional)
            
        Returns:
            (success, error): Whether successful, error message
        """
        try:
            success, errors = self.update_indicator_config(name, config_dict, chart_id)  # type: ignore
            if success:
                return True, None
            else:
                return False, "; ".join(errors)
        except Exception as e:
            error_msg = f"Exception while updating indicator config: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg
    
    async def remote_recalculate_indicator(self, name: str, chart_id: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        """
        Remote recalculate indicator
        
        Args:
            name: Indicator name
            chart_id: Chart ID (optional)
            
        Returns:
            (success, error): Whether successful, error message
        """
        try:
            return await self.recalculate_indicator(name, chart_id)  # type: ignore
        except Exception as e:
            error_msg = f"Exception while recalculating indicator: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg
    
    def remote_get_indicator_info(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all indicator information (remote call)
        
        Returns:
            Dict: Indicator information
        """
        registry = IndicatorRegistry.get_instance()
        return registry.get_info()
