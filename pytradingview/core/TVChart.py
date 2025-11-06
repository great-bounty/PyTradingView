from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Union,
    AsyncGenerator,
    Awaitable,
    Literal,
)

from ..shapes.TVShapePoint import TVShapePoint
from ..shapes.TVBaseShape import TVBaseShape
from .TVBridge import TVBridge
from .TVBridgeObject import TVMethodResponse
from .TVObject import TVObject, CallBackParams
from ..shapes.TVShapePosition import TVShapePosition
from ..shapes.TVAnchorShape import TVAnchorShape
from ..trading.TVExecutionLine import TVExecutionLine
from ..shapes.TVShape import TVShape
from ..trading.TVOrderLine import TVOrderLine
from ..trading.TVPositionLine import TVPositionLine
from ..models.TVStudy import TVStudy
from ..models.TVTimeScale import TVTimeScale
from ..models.TVTimezone import TVTimezone
from ..shapes.TVMultipleShape import TVMultipleShape
from ..shapes.TVSingleShape import TVSingleShape
from .TVSubscription import TVSubscription
from ..shapes.TVShapesGroupController import TVShapesGroupController
from ..models.TVPane import TVPane
from ..models.TVSeries import TVSeries
from ..shapes.TVSelection import TVSelection
import sys
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 类型别名（简化）
SeriesType = Literal[
    "candle", "line", "bar", "area", "heikinAshi", "hollowCandle", "baseline"
]
EntityId = str

class TVChart(TVObject):
    """Chart API object for interacting with TradingView charts.
    
    This class provides methods to control chart behavior, manage studies,
    create shapes, handle events, and customize the chart appearance.
    Each chart instance corresponds to a single chart panel in the widget.
    
    Attributes:
        setSymbolOptions: Optional callback for symbol change completion
    """
    
    def __init__(self, object_id = ""):
        super().__init__(object_id)
        self.setSymbolOptions: Optional[Callable[[], None]] = None

    async def applyLineToolsState(self, state: Any, callback: CallBackParams = None) -> None:
        """Applies line tools state to the chart to restore drawings from saved content.
            
        Requires the `saveload_separate_drawings_storage` featureset to be enabled.
            
        Args:
            state: State object containing line tools and groups
            callback: Optional callback invoked after application completes
        """
        self.applyLineToolsState_callback: CallBackParams = callback

        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"state": state}
        )
        
        logger.info(f"applyLineToolsState completed")
    
    async def applyLineToolsStateCallback(self) -> None:
        """Callback method invoked by frontend TypeScript after applyLineToolsState Promise resolves.
        
        This method is called by the remote invocation framework to notify Python
        that line tools state application has completed.
        """
        logger.info("applyLineToolsStateCallback: received from frontend")
        if hasattr(self, 'applyLineToolsState_callback') and self.applyLineToolsState_callback:
            await self.handleCallbackFunction(callback=self.applyLineToolsState_callback)

    async def applyStudyTemplate(self, template: Any) -> None:
        """Applies a study template to the chart.
        
        Args:
            template: Study template object to apply
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"template": template}
        )
        logger.info(f"applyStudyTemplate: {resp.result}")

    async def availableZOrderOperations(self, sources: Any) -> Any:
        """Returns available Z-order operations for the specified entity collection.
        
        Args:
            sources: Array of entity IDs
            
        Returns:
            Any: Available Z-order operations object
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"sources": sources}
        )
        return resp.result

    async def barTimeToEndOfPeriod(self, unixTime: int) -> int:
        """Returns the end-of-period time for the specified Unix timestamp.
            
        Args:
            unixTime: Date timestamp in seconds
                
        Returns:
            int: End-of-period timestamp
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"unixTime": unixTime}
        )
        return resp.result

    async def bringForward(self, sources: Any) -> None:
        """Moves the specified sources one level up in the Z-order.
        
        Args:
            sources: Array of source IDs
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"sources": sources}
        )
        logger.info(f"bringForward: {resp.result}")

    async def bringToFront(self, sources: Any) -> None:
        """Moves the specified sources to the top of the Z-order.
        
        Args:
            sources: Array of source IDs
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"sources": sources}
        )
        logger.info(f"bringToFront: {resp.result}")

    async def canZoomOut(self) -> bool:
        """Checks whether the chart can be zoomed out using the zoomOut method.
        
        Returns:
            bool: True if zoom out is possible
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def cancelSelectBar(self) -> None:
        """Cancels any active bar selection request.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        logger.info(f"cancelSelectBar: {resp.result}")

    async def chartType(self) -> SeriesType:
        """Returns the chart type of the main series.
            
        Returns:
            SeriesType: Chart type (e.g., 'candle', 'line', 'bar', 'area')
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def clearMarks(self, marksToClear: Any = None) -> None:
        """Removes marks from the chart.
            
        Args:
            marksToClear: Types of marks to clear. If not specified, clears both
                         bar marks and timescale marks
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"marksToClear": marksToClear},
        )
        logger.info(f"clearMarks: {resp.result}")

    async def createAnchoredShape(self, position: TVShapePosition, options: TVAnchorShape) -> EntityId:
        """Creates a new anchored shape that maintains relative position as chart range changes.
            
        Args:
            position: Percentage coordinates (x, y) relative to chart top-left corner
            options: Shape options object
                
        Returns:
            EntityId: Entity ID of the new shape
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"position": position.to_json(), "options": options.to_json()},
        )
        return resp.result

    async def createExecutionShape(
        self, options: Any = None
    ) -> TVExecutionLine:
        """Creates a new trading execution marker on the chart.
        
        Only available on Trading Platform with version >= 29.
        
        Args:
            options: Undo options
            
        Returns:
            TVExecutionLine: Trading execution line adapter
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        return TVExecutionLine.get_or_create(object_id=resp.result)

    async def createMultipointShape(self, points: list[TVShapePoint], options: TVMultipleShape) -> EntityId:
        """Creates a multi-point shape (such as a trend line).
            
        Args:
            points: Array of points defining the shape
            options: Shape options object
                
        Returns:
            EntityId: Entity ID of the new shape
        """
        point_infos: list[dict[Any, Any]] = [point.to_json() for point in points]
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"points": point_infos, "options": options.to_json()},
        )
        return resp.result

    async def createOrderLine(self, options: Any = None) -> TVOrderLine:
        """Creates a new trading order line.
        
        Only available on Trading Platform with version >= 29.
        
        Args:
            options: Undo options
            
        Returns:
            TVOrderLine: Order line adapter
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        return TVOrderLine.get_or_create(object_id=resp.result)

    async def createPositionLine(self, options: Any = None) -> TVPositionLine:
        """Creates a new trading position line.
        
        Only available on Trading Platform with version >= 29.
        
        Args:
            options: Undo options
            
        Returns:
            TVPositionLine: Position line adapter
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"options": options}
        )
        return TVPositionLine.get_or_create(resp.result)

    async def createShape(self, point: TVShapePoint, options: TVSingleShape) -> EntityId:
        """Creates a single-point shape (such as a vertical line).
            
        Args:
            point: Shape position point
            options: Shape options object
                
        Returns:
            EntityId: Entity ID of the new shape
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name,
            kwargs={"point": point.to_json(), "options": options.to_json()},
        )
        return resp.result

    async def createStudy(
        self,
        name: str,
        forceOverlay: Optional[bool] = None,
        lock: Optional[bool] = None,
        inputs: Optional[Dict[str, Any]] = None,
        overrides: Optional[Any] = None,
        options: Optional[Any] = None,
        callback: Optional[CallBackParams] = None,
    ) -> None:
        """Adds an indicator or comparison symbol to the chart.
            
        Args:
            name: Indicator name (e.g., "Moving Average")
            forceOverlay: Whether to force the indicator into the main pane
            lock: Whether to lock the indicator (user cannot delete/hide/modify)
            inputs: Indicator input parameters (named property object)
            overrides: Indicator style override parameters
            options: Additional options for creating the indicator
            callback: Optional callback called when study is created
                
        Returns:
            str: Entity ID of the new indicator
        """
        self.createStudy_callback: CallBackParams = callback
        kwargs = {
            "name": name,
            "forceOverlay": forceOverlay,
            "lock": lock,
            "inputs": inputs,
            "overrides": overrides,
            "options": options,
        }
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result
    
    async def createStudyCallback(self, entityId: str) -> None:
        """Callback method invoked when a study is created.
        
        Args:
            entityId: Entity ID of the created study
        """
        if self.createStudy_callback:
            await self.handleCallbackFunction(callback=self.createStudy_callback, entityId=entityId)
        

    async def createStudyTemplate(self, options: Any) -> dict:
        """Saves the current study template to an object.
            
        Args:
            options: Template options (e.g., whether to save symbol, interval, etc.)
                
        Returns:
            dict: Study template object
        """
        kwargs = {"options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def crossHairMoved(self) -> None:
        """Returns a subscription for crosshair movement on the chart.
            
        Note: Current Python implementation only triggers the bridge call.
        Actual event listening needs to be handled on the frontend.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"crossHairMoved: {resp.result}")

    async def dataReady(self) -> bool:
        """Provides a callback to be invoked when chart data loading completes.
            
        If data is already loaded, the callback is invoked immediately.
            
        Returns:
            bool: True if data is ready, False otherwise
        """
        kwargs = {"callback": "dataReadyCallback"}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def dataReadyCallback(self) -> None:
        """Internal callback function for dataReady.
        """
        pass

    async def endOfPeriodToBarTime(self, unixTime: int) -> int:
        """Converts end-of-period time to bar timestamp.
            
        Args:
            unixTime: Date timestamp in seconds
                
        Returns:
            int: Corresponding bar timestamp
        """
        kwargs = {"unixTime": unixTime}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def executeActionById(self, actionId: str) -> None:
        """Executes an action by ID (such as undo, opening drawing toolbar, etc.).
            
        Args:
            actionId: Action ID (e.g., "undo", "drawingToolbarAction")
        """
        kwargs = {"actionId": actionId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"executeActionById: {resp.result}")

    async def exportData(self, options: Optional[Any] = None, callback: CallBackParams = None) -> None:
        """Exports current chart data.
            
        Args:
            options: Export options (controls which data to export)
            callback: Optional callback invoked with exported data
                
        Returns:
            Any: Exported data
        """
        self.exportData_callback: CallBackParams = callback
        kwargs = {"options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def exportDataCallback(self, exportedData: Any) -> None:
        """Callback method invoked with exported chart data.
        
        Args:
            exportedData: The exported data from the chart
        """
        if self.exportData_callback:
            await self.handleCallbackFunction(callback=self.exportData_callback, exportedData=exportedData)

    async def getAllPanesHeight(self) -> List[int]:
        """Returns an array of all pane heights.
            
        Returns:
            List[int]: Array of heights in pixels
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def getAllShapes(self) -> List[Dict[str, Any]]:
        """Returns ID and name information for all shapes on the chart.
        
        Returns:
            List[Dict[str, Any]]: Array of shape information
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def getAllStudies(self) -> List[Dict[str, Any]]:
        """Returns ID and name information for all studies (indicators) on the chart.
            
        Returns:
            List[Dict[str, Any]]: Array of study information
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def getCheckableActionState(self, actionId: str) -> Optional[bool]:
        """Returns the current state of a checkable action.
            
        Args:
            actionId: Action ID
                
        Returns:
            Optional[bool]: None if action doesn't exist or isn't checkable,
                          otherwise returns boolean value
        """
        kwargs = {"actionId": actionId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def getLineToolsState(self) -> Any:
        """Returns the current chart's line tools state (including all drawings).
            
        Requires the `saveload_separate_drawings_storage` featureset to be enabled.
            
        Returns:
            Any: Line tools and groups state object
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def getPanes(self) -> List[TVPane]:
        """Returns an array of pane API objects.
        
        Returns:
            List[TVPane]: Array of pane API objects
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        # resp.result 应该是一个 object_id数组
        if isinstance(resp.result, list):
            return [TVPane.get_or_create(object_id=pane_id) for pane_id in resp.result]
        return []

    async def getPriceToBarRatio(self) -> Optional[float]:
        """Returns the chart's price-to-bar ratio.
            
        Returns:
            Optional[float]: Ratio value, or None if undefined
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def getSeries(self) -> TVSeries:
        """Returns the API object for the main series.
        
        Returns:
            TVSeries: Main series API object
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSeries.get_or_create(object_id=resp.result)

    async def getShapeById(self, entityId: str) -> TVShape:
        """Returns a shape object by entity ID.
        
        Args:
            entityId: Shape ID
            
        Returns:
            TVShape: Shape data source API object
        """
        kwargs = {"entityId": entityId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVShape.get_or_create(object_id=resp.result)

    async def getStudyById(self, entityId: str) -> TVStudy:
        """Returns a study (indicator) object by entity ID.
            
        Args:
            entityId: Study ID
                
        Returns:
            TVStudy: Study API object
        """
        kwargs = {"entityId": entityId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVStudy.get_or_create(object_id=resp.result)

    async def getTimeScale(self) -> TVTimeScale:
        """Returns the time scale API object.
        
        Returns:
            TVTimeScale: Time scale API object
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVTimeScale.get_or_create(object_id=resp.result)

    async def getTimezoneApi(self) -> TVTimezone:
        """Returns the timezone API object.
        
        Returns:
            TVTimezone: Timezone API object
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVTimezone.get_or_create(object_id=resp.result)

    async def getVisibleRange(self) -> Any:
        """Returns the currently visible time range.
            
        Returns:
            Any: Visible time range object (contains from/to timestamps)
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def isMaximized(self) -> bool:
        """Checks whether the current chart is in a maximized state.
        
        Returns:
            bool: True if maximized
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def isPriceToBarRatioLocked(self) -> bool:
        """Returns whether the chart's price-to-bar ratio is locked.
        
        Returns:
            bool: True if locked
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def isSelectBarRequested(self) -> bool:
        """Checks whether bar selection mode has been requested.
        
        Returns:
            bool: True if requested
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def loadChartTemplate(self, templateName: str, callback: CallBackParams = None) -> None:
        """Loads and applies a chart template by name.
            
        Args:
            templateName: Template name
            callback: Optional callback invoked after loading completes
        """
        self.loadChartTemplate_callback: CallBackParams = callback
        
        kwargs = {"templateName": templateName}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        
        logger.info(f"loadChartTemplate completed: template={templateName}")

    async def loadChartTemplateCallback(self) -> None:
        """Callback method invoked by frontend TypeScript after loadChartTemplate Promise resolves.
        
        This method is called by the remote invocation framework to notify Python
        that chart template loading has completed.
        """
        logger.info("loadChartTemplateCallback: received from frontend")
        if hasattr(self, 'loadChartTemplate_callback') and self.loadChartTemplate_callback:
            await self.handleCallbackFunction(callback=self.loadChartTemplate_callback)

    async def marketStatus(self) -> Any:
        """Returns a read-only observable value for market status.
            
        Returns:
            Any: Market status object (read-only)
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def maximizeChart(self) -> None:
        """Maximizes the currently selected chart to fullscreen.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"maximizeChart: {resp.result}")

    async def onChartTypeChanged(self) -> TVSubscription:
        """Subscribes to chart type change events.
            
        Returns:
            TVSubscription: Subscription object for chart type changes
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSubscription.get_or_create(object_id=resp.result)

    async def onDataLoaded(self) -> TVSubscription:
        """Subscribes to chart new data loading completion events.
        
        Returns:
            TVSubscription: Subscription object for data loading completion
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSubscription.get_or_create(object_id=resp.result)

    async def onHoveredSourceChanged(self) -> TVSubscription:
        """Subscribes to crosshair hovered study or series ID change events.
            
        Returns:
            TVSubscription: Subscription object for hovered source ID changes
                          (None when not hovering)
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSubscription.get_or_create(resp.result)

    async def onIntervalChanged(self) -> TVSubscription:
        """Subscribes to chart interval (resolution) change events.
            
        Can also be used to intercept time range changes.
            
        Returns:
            TVSubscription: Subscription object for interval changes
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSubscription.get_or_create(resp.result)

    async def onSymbolChanged(self) -> TVSubscription:
        """Subscribes to chart symbol change events.
        
        Returns:
            TVSubscription: Subscription object for symbol changes
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSubscription.get_or_create(resp.result)

    async def onVisibleRangeChanged(self) -> TVSubscription:
        """Subscribes to chart visible time range change events.
        
        Returns:
            TVSubscription: Subscription object for visible range changes
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSubscription.get_or_create(resp.result)

    async def priceFormatter(self) -> Any:
        """Returns a price formatter object for formatting price display.
            
        Returns:
            Any: Price formatter (contains format method)
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def refreshMarks(self) -> None:
        """Forces the chart to re-request all bar marks and timescale marks.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"refreshMarks: {resp.result}")

    async def reloadLineToolsFromServer(self) -> None:
        """Manually triggers reloading line tools from the server.
            
        Requires saveload_separate_drawings_storage to be enabled.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"reloadLineToolsFromServer: {resp.result}")

    async def removeAllShapes(self) -> None:
        """Removes all shapes from the chart.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"removeAllShapes: {resp.result}")

    async def removeAllStudies(self) -> None:
        """Removes all studies (indicators) from the chart.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"removeAllStudies: {resp.result}")

    async def removeEntity(self, entityId: Any, options: Optional[Any] = None) -> None:
        """Removes the specified entity (shape or study) from the chart.
            
        Args:
            entityId: Entity ID
            options: Undo options (optional)
        """
        kwargs = {"entityId": entityId, "options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"removeEntity: {resp.result}")

    async def requestSelectBar(self, callback: CallBackParams) -> None:
        """Requests to enter bar selection mode.
            
        Returns the timestamp of the bar when the user clicks on it.
            
        Args:
            callback: Callback invoked with selected bar's timestamp
                
        Returns:
            int: User-selected bar timestamp (Promise), rejects if canceled
        """
        self.requestSelectBar_callback: CallBackParams = callback
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def requestSelectBarCallback(self, unixTime: int) -> None:
        if self.requestSelectBar_callback:
            await self.handleCallbackFunction(callback=self.requestSelectBar_callback, unixTime=unixTime)

    async def resetData(self) -> None:
        """Forces the chart to re-request data (e.g., after network recovery).
            
        It's recommended to call resetCache first.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"resetData: {resp.result}")

    async def resolution(self) -> Any:
        """Returns the current chart interval (resolution).
            
        Returns:
            Any: Current interval string (e.g., "1D", "5")
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def restoreChart(self) -> None:
        """Restores the currently selected chart to its original size.
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"restoreChart: {resp.result}")

    async def selection(self) -> TVSelection:
        """Returns the selection API object for managing shape selection.
            
        Returns:
            TVSelection: Selection API object
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVSelection.get_or_create(object_id=resp.result)

    async def sendBackward(self, sources: List[Any]) -> None:
        """Moves the specified sources one level down in the Z-order.
        
        Args:
            sources: Array of source IDs
        """
        kwargs = {"sources": sources}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"sendBackward: {resp.result}")

    async def sendToBack(self, entities: List[Any]) -> None:
        """Moves the specified entity group to the bottom of the Z-order.
        
        Args:
            entities: Array of entity IDs
        """
        kwargs = {"entities": entities}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"sendToBack: {resp.result}")

    async def setAllPanesHeight(self, heights: List[int]) -> None:
        """Sets the height of each pane (in order).
            
        Args:
            heights: Array of heights in pixels
        """
        kwargs = {"heights": heights}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setAllPanesHeight: {resp.result}")

    async def setChartType(
        self, type: Any, callback: Optional[Callable[[], None]] = None
    ) -> None:
        """Sets the chart type (e.g., candlestick, line chart, etc.).
            
        Args:
            type: Chart type (SeriesType enum value)
            callback: Optional callback invoked after type change and loading complete
        """
        kwargs = {"type": type, "callback": callback}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setChartType: {resp.result}")

    async def setDragExportEnabled(self, enabled: bool) -> None:
        """Enables or disables drag export functionality.
        
        Args:
            enabled: Whether to enable drag export
        """
        kwargs = {"enabled": enabled}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setDragExportEnabled: {resp.result}")

    async def setPriceToBarRatio(
        self, ratio: float, options: Optional[Any] = None
    ) -> None:
        """Sets the chart's price-to-bar ratio.
            
        Args:
            ratio: New ratio value
            options: Undo options (optional)
        """
        kwargs = {"ratio": ratio, "options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setPriceToBarRatio: {resp.result}")

    async def setPriceToBarRatioLocked(
        self, value: bool, options: Optional[Any] = None
    ) -> None:
        """Locks or unlocks the chart's price-to-bar ratio.
            
        Args:
            value: Whether to lock
            options: Undo options (optional)
        """
        kwargs = {"value": value, "options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setPriceToBarRatioLocked: {resp.result}")

    async def setResolution(
        self,
        resolution: Any,
        options: Optional[Union[Any, Callable[[], None]]] = None,
        callback: CallBackParams = None
    ) -> Awaitable[bool]:
        """Sets the chart interval (resolution).
            
        Args:
            resolution: Interval string (e.g., "1D", "60")
            options: Setting options or callback function
            callback: Optional callback invoked with success status
                
        Returns:
            bool: Resolves with True if successful, False otherwise
        """
        self.setResolution_callback: CallBackParams = callback
        kwargs = {"resolution": resolution, "options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def setResolutionCallback(self, success: bool) -> None:
        if self.setResolution_callback:
            await self.handleCallbackFunction(callback=self.setResolution_callback, success=success)

    async def setScrollEnabled(self, enabled: bool) -> None:
        """Enables or disables chart scrolling.
        
        Args:
            enabled: Whether to enable scrolling
        """
        kwargs = {"enabled": enabled}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def setSymbol(
        self,
        symbol: str,
        options: Optional[Union[Any, Callable[[], None]]] = None,
    ) -> None:
        """Sets the chart's trading symbol.
            
        Args:
            symbol: Trading symbol code (e.g., "AAPL")
            options: Setting options or callback function
                
        Returns:
            bool: Resolves with True if successful, False otherwise
        """
        kwargs = {"symbol": symbol}
        self.setSymbolOptions = options
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setSymbol: {resp.result}")

    async def setSymbolOptionsCallback(self) -> None:
        """Safely executes the symbol options callback function.
        
        This method is called when symbol setting is complete.
        """
        if not (self.setSymbolOptions and callable(self.setSymbolOptions)):
            return

        try:
            self.setSymbolOptions()
        except Exception as e:
            logger.error(f"Symbol options callback failed: {str(e)}", exc_info=True)
        finally:
            logger.info("setSymbolOptionsCallback executed")

    async def setTimeFrame(self, timeFrame: Any) -> None:
        """Sets the chart's time frame.
            
        Args:
            timeFrame: Time frame options (contains type, value, resolution, etc.)
        """
        kwargs = {"timeFrame": timeFrame}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setTimeFrame: {resp.result}")

    async def setVisibleRange(
        self,
        range: Any,
        options: Optional[Any] = None,
        callback: CallBackParams = None,
    ) -> None:
        """Sets the chart's visible time range.
            
        Args:
            range: Time range to display (from/to timestamps)
            options: Visible range setting options (e.g., right margin percentage)
            callback: Optional callback invoked after setting completes
        """
        self.setVisibleRange_callback: CallBackParams = callback
        
        kwargs = {"range": range, "options": options}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        
        logger.info(f"setVisibleRange completed")

    async def setVisibleRangeCallback(self) -> None:
        """Callback method invoked by frontend TypeScript after setVisibleRange Promise resolves.
        
        This method is called by the remote invocation framework to notify Python
        that visible range setting has completed.
        """
        logger.info("setVisibleRangeCallback: received from frontend")
        if hasattr(self, 'setVisibleRange_callback') and self.setVisibleRange_callback:
            await self.handleCallbackFunction(callback=self.setVisibleRange_callback)

    async def setZoomEnabled(self, enabled: bool) -> None:
        """Enables or disables chart zooming.
        
        Args:
            enabled: Whether to enable zooming
        """
        kwargs = {"enabled": enabled}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"setZoomEnabled: {resp.result}")

    async def shapesGroupController(self) -> TVShapesGroupController:
        """Returns the shapes group controller API.
        
        Returns:
            TVShapesGroupController: Shapes group controller
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return TVShapesGroupController.get_or_create(resp.result)

    async def showPropertiesDialog(self, studyId: Any) -> None:
        """Displays the properties dialog for the specified study or shape.
        
        Args:
            studyId: Entity ID of the study or shape
        """
        kwargs = {"studyId": studyId}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"showPropertiesDialog: {resp.result}")

    async def symbol(self) -> str:
        """Returns the current chart's trading symbol name.
            
        Returns:
            str: Trading symbol string (e.g., "BTCUSD")
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def symbolExt(self) -> Optional[Any]:
        """Returns extended information for the current chart's trading symbol.
        
        Returns:
            Optional[Any]: Trading symbol extended information object
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        return resp.result

    async def zoomOut(self) -> None:
        """Executes a chart zoom out operation (equivalent to clicking the 'Zoom Out' button).
        """
        kwargs = {}
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs=kwargs
        )
        logger.info(f"zoomOut: {resp.result}")
