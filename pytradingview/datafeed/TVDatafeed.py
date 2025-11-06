"""
TradingView Datafeed API Python Implementation
Based on charting_library datafeed-api.d.ts specification.
"""

from typing import Any, Dict, List, Optional, Callable
import logging

# Import all modular components
from .TVTypes import ResolutionString
from .TVDataStructures import (
    TVBar, TVHistoryMetadata, TVDatafeedConfiguration,
    TVPeriodParams, TVDOMData
)
from .TVSymbolInfo import (
    TVLibrarySymbolInfo, TVSearchSymbolResultItem, TVSymbolResolveExtension
)
from .TVMarks import TVMark, TVTimescaleMark
from .TVQuotes import TVQuoteData, TVDatafeedQuoteValues
from .TVCallbacks import *
from .TVInterfaces import (
    TVIExternalDatafeed, TVIDatafeedChartApi, TVIDatafeedQuotesApi
)

# Re-export for backward compatibility
Bar = TVBar
HistoryMetadata = TVHistoryMetadata
DatafeedConfiguration = TVDatafeedConfiguration
LibrarySymbolInfo = TVLibrarySymbolInfo
SearchSymbolResultItem = TVSearchSymbolResultItem
SymbolResolveExtension = TVSymbolResolveExtension
PeriodParams = TVPeriodParams
Mark = TVMark
TimescaleMark = TVTimescaleMark
DOMData = TVDOMData
DatafeedQuoteValues = TVDatafeedQuoteValues
QuoteData = TVQuoteData
IExternalDatafeed = TVIExternalDatafeed
IDatafeedChartApi = TVIDatafeedChartApi
IDatafeedQuotesApi = TVIDatafeedQuotesApi

logger = logging.getLogger(__name__)

# ============= TVDatafeed Implementation =============

class TVDatafeed(TVIExternalDatafeed, TVIDatafeedChartApi, TVIDatafeedQuotesApi):
    """
    TradingView Datafeed Complete Implementation
    
    This is a complete implementation of the TradingView datafeed API
    that combines external datafeed, chart API, and quotes API interfaces.
    Subclasses should override specific methods to provide actual data.
    """

    def __init__(self):
        self._configuration: Optional[TVDatafeedConfiguration] = None
        self._subscribers: Dict[str, Any] = {}
        self._quote_subscribers: Dict[str, Any] = {}
        logger.info("TVDatafeed initialized")

    # ========== IExternalDatafeed Implementation ==========

    def onReady(self, callback: TVOnReadyCallback) -> None:
        """
        Provides datafeed configuration to the library.
        Subclasses should override this method to provide actual configuration.
        """
        if self._configuration is None:
            self._configuration = TVDatafeedConfiguration()
        callback(self._configuration)

    # ========== IDatafeedChartApi Implementation ==========

    def searchSymbols(
        self,
        userInput: str,
        exchange: str,
        symbolType: str,
        onResult: TVSearchSymbolsCallback
    ) -> None:
        """Search for symbols - should be implemented by subclass."""
        logger.warning("searchSymbols not implemented")
        onResult([])

    def resolveSymbol(
        self,
        symbolName: str,
        onResolve: TVResolveCallback,
        onError: TVDatafeedErrorCallback,
        extension: Optional[TVSymbolResolveExtension] = None
    ) -> None:
        """Resolve symbol information - should be implemented by subclass."""
        logger.warning("resolveSymbol not implemented")
        onError("resolveSymbol not implemented")

    def getBars(
        self,
        symbolInfo: TVLibrarySymbolInfo,
        resolution: ResolutionString,
        periodParams: TVPeriodParams,
        onResult: TVHistoryCallback,
        onError: TVDatafeedErrorCallback
    ) -> None:
        """Get historical bars - should be implemented by subclass."""
        logger.warning("getBars not implemented")
        onResult([], TVHistoryMetadata(noData=True))

    def subscribeBars(
        self,
        symbolInfo: TVLibrarySymbolInfo,
        resolution: ResolutionString,
        onTick: TVSubscribeBarsCallback,
        listenerGuid: str,
        onResetCacheNeededCallback: Callable[[], None]
    ) -> None:
        """Subscribe to real-time bar updates - should be implemented by subclass."""
        self._subscribers[listenerGuid] = {
            'symbolInfo': symbolInfo,
            'resolution': resolution,
            'onTick': onTick,
            'onReset': onResetCacheNeededCallback
        }
        logger.info(f"Subscribed bars for {symbolInfo.name} with ID {listenerGuid}")

    def unsubscribeBars(self, listenerGuid: str) -> None:
        """Unsubscribe from bar updates."""
        if listenerGuid in self._subscribers:
            del self._subscribers[listenerGuid]
            logger.info(f"Unsubscribed bars with ID {listenerGuid}")

    # ========== IDatafeedQuotesApi Implementation ==========

    def getQuotes(
        self,
        symbols: List[str],
        onDataCallback: TVQuotesCallback,
        onErrorCallback: TVQuotesErrorCallback
    ) -> None:
        """Get quote data - should be implemented by subclass."""
        logger.warning("getQuotes not implemented")
        onDataCallback([])

    def subscribeQuotes(
        self,
        symbols: List[str],
        fastSymbols: List[str],
        onRealtimeCallback: TVQuotesCallback,
        listenerGUID: str
    ) -> None:
        """Subscribe to real-time quotes - should be implemented by subclass."""
        self._quote_subscribers[listenerGUID] = {
            'symbols': symbols,
            'fastSymbols': fastSymbols,
            'callback': onRealtimeCallback
        }
        logger.info(f"Subscribed quotes with ID {listenerGUID}")

    def unsubscribeQuotes(self, listenerGUID: str) -> None:
        """Unsubscribe from quote updates."""
        if listenerGUID in self._quote_subscribers:
            del self._quote_subscribers[listenerGUID]
            logger.info(f"Unsubscribed quotes with ID {listenerGUID}")
