from __future__ import annotations
import asyncio
import sys
import logging

from .TVObject import CallBackParams
from ..ui.TVDropdownApi import TVDropdownApi
from ..ui.TVHMElement import TVHMElement
from typing import Any, Callable, Dict, List, Optional, Union, AsyncGenerator, Awaitable, Coroutine
from .TVObject import TVObject, CallBackParams
from .TVBridgeObject import TVMethodResponse
from .TVChart import TVChart
from ..ui.TVContextMenuItem import TVContextMenuItem
from .TVWatchedValue import TVWatchedValue
from .TVCustomSymbolStatus import TVCustomSymbolStatus
from .TVCustomThemes import TVCustomThemes

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ================
# Main Widget Proxy Class
# ================
class TVWidget(TVObject):
    """Main class for interacting with TradingView Chart Widget.
    
    This class provides a Python interface to the TradingView Widget API,
    allowing you to create, configure, and interact with TradingView charts.
    It mirrors the functionality of the JavaScript ChartingLibraryWidgetConstructor.
    
    Note: Configuration and callbacks are now managed by TVEngine via TVBridge.
    """

    def __init__(self, object_id: str):
        super().__init__(object_id)
        self.onShortcutInfos: list[dict[str, Any]] = []
        self.event_callbacks: Dict[str, List[CallBackParams]] = {}
    
    async def activeChart(self) -> TVChart:
        """Returns the chart API object for the currently active chart.
        
        Can be used to subscribe to chart events (such as interval changes).
        Note: When switching multi-chart layouts, you need to manually unsubscribe 
        from the old chart and subscribe to the new chart.
        It is recommended to use this in combination with the `activeChartChanged` event.
        
        Returns:
            TVChart: The active chart API object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVChart.get_or_create(resp.result)

    async def activeChartIndex(self) -> int:
        """Returns the index of the currently active chart in the layout (0-based).
        
        Returns:
            int: The zero-based index of the active chart
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def addCustomCSSFile(self, url: str) -> None:
        """Loads a custom CSS file.
        
        Args:
            url: Absolute URL of the CSS file or relative path to the static folder
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"url": url}
        )
        logger.info(f"addCustomCSSFile: {resp.result}")

    async def applyOverrides(self, overrides: Dict[str, Any]) -> None:
        """Applies chart property overrides without reloading the chart.
        
        Args:
            overrides: Dictionary of property overrides to apply
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"overrides": overrides}
        )
        logger.info(f"applyOverrides: {resp.result}")

    async def applyStudiesOverrides(self, overrides: Dict[str, Any]) -> None:
        """Applies study (indicator) style and input overrides without reloading.
        
        Args:
            overrides: Study override configuration object, see StudyOverrides
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"overrides": overrides}
        )
        logger.info(f"applyStudiesOverrides: {resp.result}")

    async def applyTradingCustomization(self, config: Dict[str, Any]) -> None:
        """Applies trading customization settings (for order/position line styling, etc.).
        
        Args:
            config: Trading customization configuration
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"config": config}
        )
        logger.info(f"applyTradingCustomization: {resp.result}")

    async def changeTheme(self, theme_name: str, options: Optional[Dict] = None, callback: CallBackParams = None) -> None:
        """Changes the chart theme.
        
        Args:
            theme_name: Name of the theme to apply
            options: Optional theme configuration
            callback: Optional callback function called after theme change completes
        """
        self.changeTheme_callback: CallBackParams = callback

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"theme_name": theme_name, "options": options},
        )
        logger.info(f"changeTheme: {resp.result}")

    async def changeThemeCallback(self) -> None:
        """Callback method invoked by frontend TypeScript after changeTheme Promise resolves.
        
        This method is called by the remote invocation framework to notify Python 
        that the theme change has completed.
        
        Note: This is a synchronous method called by the remote invocation framework.
        """
        logger.info("changeThemeCallback: received from frontend")
        if self.changeTheme_callback:
            await self.handleCallbackFunction(callback=self.changeTheme_callback)

    async def chart(self, index: int = 0) -> TVChart:
        """Returns the chart API instance at the specified index.
        
        Args:
            index: Chart index (0-based), defaults to currently active chart
            
        Returns:
            TVChart: The chart API object at the specified index
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"index": index}
        )
        return TVChart.get_or_create(resp.result)

    async def chartsCount(self) -> int:
        """Returns the number of charts in the current layout.
        
        Returns:
            int: Number of charts in the layout
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def clearUndoHistory(self) -> None:
        """Clears the undo/redo history.
        
        Warning: Only use this in specific scenarios (e.g., when reusing charts
        during SPA page transitions).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"clearUndoHistory: {resp.result}")

    async def closePopupsAndDialogs(self) -> None:
        """Closes all open context menus, popups, or dialogs.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"closePopupsAndDialogs: {resp.result}")

    async def createButton(self, options: Dict[str, Any]) -> TVHMElement:
        """Creates a button on the top toolbar.
        
        Args:
            options: Button configuration options. Can include:
                - text: Button text
                - title: Tooltip text
                - onClick: Callback function (will be registered automatically)
                - useTradingViewStyle: Whether to use TradingView styling
                - align: Alignment ('left' or 'right')
                - icon: SVG icon markup
                
        Returns:
            TVHMElement: Button element that can be further customized
            
        Example:
            ```python
            button = await widget.createButton({
                'text': 'My Button',
                'onClick': lambda: print('Clicked!')
            })
            ```
        """
        onClick = options.pop("onClick", None)
        if onClick is not None:
            options["onClick"] = "onClickCallback"
            
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        button: TVHMElement = TVHMElement.get_or_create(object_id=resp.result)
        
        if onClick is not None:
            await button.onClick(onClick)

        return button

    async def createDropdown(
        self, 
        title: str,
        items: List[Dict[str, Any]],
        tooltip: Optional[str] = None,
        icon: Optional[str] = None,
        align: Optional[str] = None
    ) -> TVDropdownApi:
        """Creates a dropdown menu on the top toolbar.
        
        Args:
            title: Dropdown menu title
            items: List of menu items, each should contain:
                - 'title' (str): Menu item title
                - 'onSelect' (callable): Click callback function (optional)
            tooltip: Dropdown tooltip text (optional)
            icon: Dropdown icon (SVG markup) (optional)
            align: Dropdown alignment, "left" or "right" (optional)
            
        Returns:
            TVDropdownApi: Dropdown API object for further manipulation
            
        Example:
            ```python
            dropdown = await widget.createDropdown(
                title='Actions',
                items=[
                    {'title': 'Option 1', 'onSelect': lambda: print('1')},
                    {'title': 'Option 2', 'onSelect': lambda: print('2')}
                ]
            )
            ```
        """
        self.dropdown_items_callbacks: List[CallBackParams] = []
        
        processed_items: list[Any] = []
        for item in items:
            item_title = item.get("title", "")
            on_select: Any | None = item.get("onSelect")
            
            self.dropdown_items_callbacks.append(on_select)
            processed_items.append({"title": item_title})
        
        params: dict[str, Any] = {
            "title": title,
            "items": processed_items
        }
        
        if tooltip is not None:
            params["tooltip"] = tooltip
        if icon is not None:
            params["icon"] = icon
        if align is not None:
            params["align"] = align
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"params": params}
        )
        
        dropdown_api: TVDropdownApi = TVDropdownApi.get_or_create(object_id=resp.result)
        return dropdown_api

    async def onDropdownItemSelect(self, index: int, title: str) -> None:
        """Callback method invoked when a dropdown menu item is clicked.
        
        This method is called by the frontend TypeScript code.
        
        Args:
            index: Index of the clicked menu item
            title: Title of the clicked menu item
        """
        logger.info(f"onDropdownItemSelect: index={index}, title={title}")
        
        if hasattr(self, 'dropdown_items_callbacks') and \
           0 <= index < len(self.dropdown_items_callbacks):
            callback: CallBackParams = self.dropdown_items_callbacks[index]
            if callback is not None:
                await self.handleCallbackFunction(callback, index=index, title=title)

    async def crosshairSync(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for cross-chart crosshair synchronization state.
        
        Trading Platform only. When enabled, moving crosshair on one chart will
        synchronize it across all charts.
        
        Returns:
            TVWatchedValue[bool]: Watched value for crosshair sync state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(object_id=resp.result)

    async def currencyAndUnitVisibility(self) -> TVWatchedValue[Any]:
        """Returns a WatchedValue for currency and unit visibility on the price axis.
        
        Returns:
            TVWatchedValue[Any]: Watched value for currency/unit visibility settings
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[Any].get_or_create(object_id=resp.result)

    async def customSymbolStatus(self) -> TVCustomSymbolStatus:
        """Returns the API for adding/modifying custom status items in the chart legend.
        
        This API is only available after the chart is created (headerReady).
        
        Returns:
            TVCustomSymbolStatus: Custom symbol status API
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVCustomSymbolStatus.get_or_create(object_id=resp.result)

    async def customThemes(self) -> TVCustomThemes:
        """Returns the custom themes API.
        
        Allows you to add, remove, and manage custom color themes.
        
        Returns:
            TVCustomThemes: Custom themes API
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVCustomThemes.get_or_create(object_id=resp.result)

    async def dateFormat(self) -> TVWatchedValue[str]:
        """Returns a WatchedValue for the date format setting.
        
        Returns:
            TVWatchedValue[str]: Watched value for date format (e.g., 'dd MMM \'yy')
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[str].get_or_create(resp.result)

    async def dateRangeSync(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for cross-chart date range synchronization state.
        
        Trading Platform only. When enabled, changing the visible date range on one
        chart will synchronize it across all charts.
        
        Returns:
            TVWatchedValue[bool]: Watched value for date range sync state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def drawOnAllChartsEnabled(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for the 'Draw on All Charts' mode.
            
        When enabled, newly drawn shapes will be copied to all charts
        (displayed when the ticker matches).
            
        Returns:
            TVWatchedValue[bool]: Watched value for draw on all charts mode
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def exitFullscreen(self) -> None:
        """Exits fullscreen mode (if currently in fullscreen).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"exitFullscreen: {resp.result}")

    async def getCSSCustomPropertyValue(self, name: str) -> str:
        """Returns the current value of a CSS custom property.
        
        Args:
            name: CSS custom property name (e.g., "--my-color")
            
        Returns:
            str: Property value string, or empty string if not set
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"name": name}
        )
        return resp.result

    async def getIntervals(self) -> List[str]:
        """Returns the list of supported time intervals (resolutions).
        
        Returns:
            List[str]: Array of interval strings, e.g., ['1D', '5D', '1Y']
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getLanguage(self) -> str:
        """Returns the current widget language code.
        
        Returns:
            str: Language code, e.g., 'en', 'zh', 'ru'
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getSavedCharts(self) -> List[Dict[str, Any]]:
        """Returns the list of charts saved on the server for the current user.
        
        Returns:
            List[Dict[str, Any]]: Array of chart records with metadata
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getStudiesList(self) -> List[str]:
        """Returns the list of all supported study (indicator) names.
        
        Returns:
            List[str]: Array of study names that can be used with createStudy
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getStudyInputs(self, study_name: str) -> List[Dict[str, Any]]:
        """Returns input parameter information for a specific study.
        
        Args:
            study_name: Name of the study/indicator
            
        Returns:
            List[Dict[str, Any]]: Array of input parameter information
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"study_name": study_name},
        )
        return resp.result

    async def getStudyStyles(self, study_name: str) -> Dict[str, Any]:
        """Returns style property metadata for a specific study.
        
        Args:
            study_name: Name of the study/indicator
            
        Returns:
            Dict[str, Any]: Study style information
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"study_name": study_name},
        )
        return resp.result

    async def getTheme(self) -> str:
        """Returns the current chart theme name.
        
        Returns:
            str: Theme name (e.g., 'Light', 'Dark')
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result


    async def headerReady(self, callback: CallBackParams) -> None:
        """Registers a callback to be called when the top toolbar is ready.
        
        Args:
            callback: Function to call when the toolbar is ready
        """
        self.headerReady_callback: CallBackParams = callback
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"headerReady: {resp.result}")


    async def headerReadyCallback(self) -> None:
        """Callback method invoked by frontend TypeScript after headerReady Promise resolves.
        
        This method is called by the remote invocation framework to notify Python
        that the toolbar is ready.
        
        Note: This is a synchronous method called by the remote invocation framework.
        """
        logger.info("headerReadyCallback: received from frontend")
        if self.headerReady_callback:
            await self.handleCallbackFunction(callback=self.headerReady_callback)
            self.headerReady_callback = None
        

    async def hideAllDrawingTools(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for the 'Hide All Drawing Tools' button state.
            
        Returns:
            TVWatchedValue[bool]: Watched value for hide all drawings state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def intervalSync(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for cross-chart interval synchronization state.
        
        Trading Platform only. When enabled, changing the interval on one chart
        will synchronize it across all charts.
        
        Returns:
            TVWatchedValue[bool]: Watched value for interval sync state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def layout(self) -> str:
        """Returns the current chart layout type.
        
        Returns:
            str: Layout type string (e.g., '2h' for two charts side by side)
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def layoutName(self) -> Optional[str]:
        """Returns the name of the current chart layout.
        
        Returns:
            Optional[str]: Layout name, or None if not saved
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def load(self, state: Dict[str, Any], extended_data: Optional[Dict] = None) -> None:
        """Loads chart state from an object (low-level API).
        
        Args:
            state: Chart state object to load
            extended_data: Optional metadata for saving
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"state": state, "extended_data": extended_data},
        )
        logger.info(f"load: {resp.result}")

    async def loadChartFromServer(self, record: Dict[str, Any]) -> None:
        """Loads a saved chart from the server.
        
        Args:
            record: Chart record obtained via getSavedCharts
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"record": record}
        )
        logger.info(f"loadChartFromServer: {resp.result}")

    async def lockAllDrawingTools(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for the 'Lock All Drawing Tools' button state.
            
        Returns:
            TVWatchedValue[bool]: Watched value for lock all drawings state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def magnetEnabled(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for the Magnet Mode enabled state.
        
        Returns:
            TVWatchedValue[bool]: Watched value for magnet mode state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def magnetMode(self) -> TVWatchedValue[int]:
        """Returns a WatchedValue for the Magnet Mode.
        
        Returns:
            TVWatchedValue[int]: Watched value for magnet mode setting
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[int].get_or_create(resp.result)

    async def mainSeriesPriceFormatter(self) -> Any:
        """Returns the price formatter for the main series.
        
        Returns:
            Any: Price formatter object with format methods
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def navigationButtonsVisibility(self) -> TVWatchedValue[Any]:
        """Returns a WatchedValue for navigation buttons visibility state.
        
        Returns:
            TVWatchedValue[Any]: Watched value for navigation buttons visibility
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[Any].get_or_create(resp.result)

    async def news(self) -> Any:
        """Returns the news widget API.
        
        Trading Platform only.
        
        Returns:
            Any: News API object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def onChartReady(self, callback: CallBackParams) -> None:
        """Registers a callback to be called when the chart is ready.
        
        Args:
            callback: Function to call when the chart is ready
        """
        self.onChartReady_callback: CallBackParams = callback

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"onChartReady: {resp.result}")
        
        
    async def onChartReadyCallback(self) -> None:
        logger.info("onChartReadyCallback: received from frontend")
        if self.onChartReady_callback:
            await self.handleCallbackFunction(callback=self.onChartReady_callback)
            self.onChartReady_callback = None

    async def onContextMenuProxy(self, itemList: List[TVContextMenuItem]) -> None:
        """Registers a context menu callback.
        
        Args:
            itemList: List of context menu items to display
        """
        self.onContextMenu_itemList: List[TVContextMenuItem] = itemList
        itemListProxy: list[dict[str, Any]] = [
            {
                "text": item.text,
                "position": item.position
            }
            for item in itemList
        ]
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"itemList": itemListProxy}
        )
        logger.info(f"onContextMenuProxy: {resp.result}")

    async def onContextMenuItemClick(self, index: int, text: str, unixTime: int, price: float) -> None:
        itemInfo: TVContextMenuItem = self.onContextMenu_itemList[index]

        logger.info(f"onContextMenuItemClick: {index}, {text}, {unixTime}, {price}")
        if hasattr(itemInfo, "click"):
            await self.handleCallbackFunction(callback=itemInfo.click, index=index, text=text, unixTime=unixTime, price=price)

    async def onGrayedObjectClicked(self, callback: CallBackParams) -> None:
        """Registers a callback for clicks on grayed-out tools/indicators.
        
        Args:
            callback: Function to call when a grayed object is clicked
        """
        self.onGrayedObjectClicked_callback: CallBackParams = callback

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(msg=f"onGrayedObjectClicked: {resp.result}")

    async def onGrayedObjectClickedCallback(self, obj: dict) -> None:
        if self.onGrayedObjectClicked_callback:
            await self.handleCallbackFunction(callback=self.onGrayedObjectClicked_callback, obj=obj)

    async def onShortcut(self, shortCut: Union[str, int, List[Union[str, int]]], callback: CallBackParams) -> None:
        """Registers a keyboard shortcut callback.
        
        Args:
            shortCut: Shortcut definition (string, number, or array)
            callback: Function to call when the shortcut is triggered
        """
        self.onShortcutInfos.append({"shortCut": shortCut, "callback": callback})

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"shortCut":shortCut}
        )
        logger.info(msg=f"onShortcut: {resp.result}")

    async def  onShortcutCallback(self, shortCut: Any):
        logger.info(msg=f"onShortcutCallback: {shortCut}")
        for info in self.onShortcutInfos:
            if info["shortCut"] == shortCut:
                await self.handleCallbackFunction(callback=info["callback"])
                break

    async def paneButtonsVisibility(self) -> TVWatchedValue[Any]:
        """Returns a WatchedValue for pane buttons visibility state.
        
        Returns:
            TVWatchedValue[Any]: Watched value for pane buttons visibility
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[Any].get_or_create(resp.result)

    async def remove(self) -> None:
        """Removes the entire widget and its data.
        
        After removal, the widget cannot be interacted with anymore.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"remove: {resp.result}")

    async def removeButton(self, button_id: str) -> None:
        """Removes a button from the top toolbar.
        
        Args:
            button_id: Button ID returned by createButton
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"button_id": button_id}
        )
        logger.info(f"removeButton: {resp.result}")

    async def removeChartFromServer(self, chart_id: Union[str, int]) -> None:
        """Deletes a saved chart from the server.
        
        Args:
            chart_id: Chart ID from SaveLoadChartRecord
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"chart_id": chart_id}
        )
        logger.info(f"removeChartFromServer: {resp.result}")

    async def resetCache(self) -> None:
        """Resets cached data for all symbols.
        
        Equivalent to calling onResetCacheNeededCallback for all symbol/resolution pairs.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"resetCache: {resp.result}")

    async def resetLayoutSizes(self, disable_undo: bool = False) -> None:
        """Resets the sizes of all charts in a multi-chart layout to default values.
        
        Args:
            disable_undo: Whether to exclude from undo stack
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"disable_undo": disable_undo},
        )
        logger.info(f"resetLayoutSizes: {resp.result}")

    async def save(self, options: Optional[Dict] = None) -> Dict[str, Any]:
        """Saves the current chart state to an object (low-level API).
        
        Args:
            options: Save options
            
        Returns:
            Dict[str, Any]: Saved chart state object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        return resp.result

    async def saveChartToServer(self, options: Optional[Dict] = None) -> None:
        """Saves the current chart to the server.
        
        Args:
            options: Save options
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        logger.info(f"saveChartToServer: {resp.result}")

    async def selectLineTool(self, linetool: str, options: Optional[Dict] = None) -> None:
        """Selects a drawing tool or cursor (simulates clicking the left toolbar).
        
        Args:
            linetool: Tool name (e.g., 'arrow', 'cursor', etc.)
            options: Optional parameters (e.g., icon/emoji configuration)
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"linetool": linetool, "options": options},
        )
        logger.info(f"selectLineTool: {resp.result}")

    async def selectedLineTool(self) -> str:
        """Returns the currently selected drawing tool or cursor.
        
        Returns:
            str: Name of the selected tool
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setActiveChart(self, index: int) -> None:
        """Sets the currently active chart by index.
        
        Args:
            index: Chart index (0-based). Invalid indices are ignored
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"index": index}
        )
        logger.info(f"setActiveChart: {resp.result}")

    async def setCSSCustomProperty(self, name: str, value: str) -> None:
        """Sets a CSS custom property value.
        
        Args:
            name: Property name (e.g., "--my-color")
            value: Property value
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"name": name, "value": value},
        )
        logger.info(f"setCSSCustomProperty: {resp.result}")

    async def setDebugMode(self, enabled: bool) -> None:
        """Enables/disables verbose logging of Datafeed API to the console.
        
        Args:
            enabled: Whether to enable debug mode
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enabled": enabled}
        )
        logger.info(f"setDebugMode: {resp.result}")

    async def setLayout(self, layout: str) -> None:
        """Sets the chart layout type.
        
        Args:
            layout: Layout type string (e.g., '2h' for two horizontal charts)
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"layout": layout}
        )
        logger.info(f"setLayout: {resp.result}")

    async def setLayoutSizes(self, sizes: Dict[str, Any], disable_undo: bool = False) -> None:
        """Sets the sizes of each chart in a multi-chart layout.
        
        Args:
            sizes: Size configuration object
            disable_undo: Whether to exclude from undo stack
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"sizes": sizes, "disable_undo": disable_undo},
        )
        logger.info(f"setLayoutSizes: {resp.result}")

    async def setSymbol(self, symbol: str, interval: str, callback: CallBackParams) -> None:
        """Sets the symbol and interval for the active chart.
        
        Args:
            symbol: Trading symbol (e.g., 'AAPL')
            interval: Time interval (e.g., '1D')
            callback: Callback function called after data loads
        """
        self.setSymbol_callback: CallBackParams = callback
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={
                "symbol": symbol,
                "interval": interval
            }
        )
        logger.info(f"setSymbol: {resp.result}")

    async def setSymbolCallback(self) -> None:
        if self.setSymbol_callback:
            await self.handleCallbackFunction(callback=self.setSymbol_callback)

    async def showConfirmDialog(self, params: Dict[str, Any]) -> None:
        """Displays a confirmation dialog with OK/Cancel buttons.
            
        Args:
            params: Dialog parameters
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"params": params}
        )
        logger.info(f"showConfirmDialog: {resp.result}")

    async def showLoadChartDialog(self) -> None:
        """Displays the 'Load Chart Layout' dialog.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"showLoadChartDialog: {resp.result}")

    async def showNoticeDialog(self, params: Dict[str, Any]) -> None:
        """Displays a notice dialog with only an OK button.
            
        Args:
            params: Dialog parameters
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"params": params}
        )
        logger.info(f"showNoticeDialog: {resp.result}")

    async def showSaveAsChartDialog(self) -> None:
        """Displays the 'Save Chart Layout As' dialog.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"showSaveAsChartDialog: {resp.result}")

    async def startFullscreen(self) -> None:
        """Enters fullscreen mode (if not currently in fullscreen).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"startFullscreen: {resp.result}")

    async def subscribe(self, event: str, callback: Callable[[Any], None]) -> None:
        """Subscribes to library events.
        
        Args:
            event: Event name (from SubscribeEventsMap)
            callback: Callback function (must be the same reference for unsubscribe)
        """
        if event not in self.event_callbacks:
            self.event_callbacks[event] = []
        
        self.event_callbacks[event].append(callback)
        
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"event": event}
        )
        logger.info(f"subscribe: event={event}, result={resp.result}")

    async def supportedChartTypes(self) -> Any:
        """Returns the supported chart types for the currently active chart (read-only).
        
        Returns:
            Any: Supported chart types object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def symbolInterval(self) -> dict:
        """Returns the symbol and interval of the active chart.
        
        Returns:
            dict: Object containing 'symbol' and 'interval' properties
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def symbolSync(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for cross-chart symbol synchronization state.
        
        Trading Platform only. When enabled, changing the symbol on one chart
        will synchronize it across all charts.
        
        Returns:
            TVWatchedValue[bool]: Watched value for symbol sync state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def takeClientScreenshot(self, options: Optional[Dict] = None) -> Any:
        """Takes a screenshot of the chart on the client side and returns a canvas.
        
        Args:
            options: Screenshot options
            
        Returns:
            Any: Promise that resolves with an HTMLCanvasElement
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        return resp.result

    async def takeScreenshot(self) -> None:
        """Takes a screenshot of the chart and uploads it to the server.
        
        Triggers the 'onScreenshotReady' event when complete.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"takeScreenshot: {resp.result}")

    async def timeHoursFormat(self) -> TVWatchedValue[Any]:
        """Returns a WatchedValue for the time format (hours part).
        
        Returns:
            TVWatchedValue[Any]: Watched value for time format setting
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[Any].get_or_create(resp.result)

    async def timeSync(self) -> TVWatchedValue[bool]:
        """Returns a WatchedValue for cross-chart time synchronization state.
        
        Trading Platform only. When enabled, changing the time on one chart
        will synchronize it across all charts.
        
        Returns:
            TVWatchedValue[bool]: Watched value for time sync state
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return TVWatchedValue[bool].get_or_create(resp.result)

    async def undoRedoState(self) -> Any:
        """Returns the current state of the undo/redo stack.
        
        Returns:
            Any: Undo/redo state object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def unloadUnusedCharts(self) -> None:
        """Unloads invisible charts in a multi-chart layout (releases memory).
        
        The unloaded charts will be treated as new charts when they become visible again.
        It is recommended to call this after the layout_changed event.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"unloadUnusedCharts: {resp.result}")

    async def unsubscribe(self, event: str, callback: Callable[[Any], None]) -> None:
        """Unsubscribes from library events.
        
        Args:
            event: Event name
            callback: Callback to remove (must be the same reference passed to subscribe)
        """
        if event not in self.event_callbacks:
            logger.warning(f"unsubscribe: No callbacks found for event={event}")
            return
        
        try:
            self.event_callbacks[event].remove(callback)
            
            # 如果该事件没有回调了,删除整个事件键
            if len(self.event_callbacks[event]) == 0:
                del self.event_callbacks[event]
            
            resp: TVMethodResponse = await self.call_web_object_method(
                method_name=sys._getframe(0).f_code.co_name,
                kwargs={"event": event}
            )
            logger.info(f"unsubscribe: event={event}, result={resp.result}")
        except ValueError:
            logger.warning(f"unsubscribe: Callback not found for event={event}")

    async def watchList(self) -> Any:
        """Returns the Watchlist API.
        
        Trading Platform only.
        
        Returns:
            Any: Watchlist API object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def watermark(self) -> Any:
        """Returns the watermark configuration API.
        
        Only available after the chart is ready (onChartReady).
        
        Returns:
            Any: Watermark API object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def widgetbar(self) -> Any:
        """Returns the widgetbar (right sidebar) API.
        
        Trading Platform only.
        
        Returns:
            Any: Widgetbar API object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def onWidgetEventFired(self, event: str, args: List[Any]) -> None:
        """Callback method invoked by frontend TypeScript when a widget event is fired.
        
        This method is called by the remote invocation framework to notify Python
        that a subscribed event has been triggered.
        
        Args:
            event: Event name that was fired
            args: Arguments passed to the event callback
        """
        logger.info(f"onWidgetEventFired: event={event}, args={args}")
        
        if event not in self.event_callbacks:
            logger.warning(f"onWidgetEventFired: No callbacks registered for event={event}")
            return
        
        # 调用所有注册的回调函数
        for callback in self.event_callbacks[event][:]:  # 使用切片以避免迭代时修改
            if callback is not None:
                try:
                    await self.handleCallbackFunction(callback, *args)
                except Exception as e:
                    logger.exception(f"Error in event callback for {event}: {e}")

    async def onWidgetEventUnsubscribed(self, event: str) -> None:
        """Callback method invoked by frontend TypeScript when unsubscribe is called.
        
        This is a notification callback that can be used for cleanup or logging.
        
        Args:
            event: Event name that was unsubscribed
        """
        logger.info(f"onWidgetEventUnsubscribed: event={event}")
