"""
TradingView Datafeed Interface Definitions
Abstract base classes defining the datafeed API contracts.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Callable
from .TVTypes import ResolutionString
from .TVCallbacks import *
from .TVDataStructures import TVPeriodParams
from .TVSymbolInfo import TVLibrarySymbolInfo, TVSymbolResolveExtension


class TVIExternalDatafeed(ABC):
    """External datafeed base interface."""

    @abstractmethod
    def onReady(self, callback: TVOnReadyCallback) -> None:
        """Provides the datafeed configuration."""
        pass


class TVIDatafeedChartApi(ABC):
    """Chart data API interface."""

    @abstractmethod
    def searchSymbols(self, userInput: str, exchange: str, symbolType: str, onResult: TVSearchSymbolsCallback) -> None:
        """Searches for symbols matching user input."""
        pass

    @abstractmethod
    def resolveSymbol(self, symbolName: str, onResolve: TVResolveCallback, onError: TVDatafeedErrorCallback, extension: Optional[TVSymbolResolveExtension] = None) -> None:
        """Resolves symbol name to SymbolInfo."""
        pass

    @abstractmethod
    def getBars(self, symbolInfo: TVLibrarySymbolInfo, resolution: ResolutionString, periodParams: TVPeriodParams, onResult: TVHistoryCallback, onError: TVDatafeedErrorCallback) -> None:
        """Retrieves historical bars."""
        pass

    @abstractmethod
    def subscribeBars(self, symbolInfo: TVLibrarySymbolInfo, resolution: ResolutionString, onTick: TVSubscribeBarsCallback, listenerGuid: str, onResetCacheNeededCallback: Callable[[], None]) -> None:
        """Subscribes to real-time bar updates."""
        pass

    @abstractmethod
    def unsubscribeBars(self, listenerGuid: str) -> None:
        """Unsubscribes from real-time bar updates."""
        pass

    def getMarks(self, symbolInfo: TVLibrarySymbolInfo, from_: int, to: int, onDataCallback: TVGetMarksCallback, resolution: ResolutionString) -> None:
        """Gets marks for visible bars range (optional)."""
        pass

    def getTimescaleMarks(self, symbolInfo: TVLibrarySymbolInfo, from_: int, to: int, onDataCallback: TVGetMarksCallback, resolution: ResolutionString) -> None:
        """Gets timescale marks (optional)."""
        pass

    def getServerTime(self, callback: TVServerTimeCallback) -> None:
        """Gets server time (optional)."""
        pass

    def subscribeDepth(self, symbol: str, callback: TVDOMCallback) -> str:
        """Subscribes to depth data (optional)."""
        return ""

    def unsubscribeDepth(self, subscriberUID: str) -> None:
        """Unsubscribes from depth data (optional)."""
        pass

    def getVolumeProfileResolutionForPeriod(self, currentResolution: ResolutionString, from_: int, to: int, symbolInfo: TVLibrarySymbolInfo) -> ResolutionString:
        """Gets resolution for Volume Profile (optional)."""
        return currentResolution


class TVIDatafeedQuotesApi(ABC):
    """Quotes datafeed API interface."""

    @abstractmethod
    def getQuotes(self, symbols: List[str], onDataCallback: TVQuotesCallback, onErrorCallback: TVQuotesErrorCallback) -> None:
        """Retrieves quote data."""
        pass

    @abstractmethod
    def subscribeQuotes(self, symbols: List[str], fastSymbols: List[str], onRealtimeCallback: TVQuotesCallback, listenerGUID: str) -> None:
        """Subscribes to real-time quotes."""
        pass

    @abstractmethod
    def unsubscribeQuotes(self, listenerGUID: str) -> None:
        """Unsubscribes from quotes."""
        pass


__all__ = [
    "TVIExternalDatafeed",
    "TVIDatafeedChartApi",
    "TVIDatafeedQuotesApi",
]
