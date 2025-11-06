"""
TradingView Datafeed Basic Data Structures
Core data structures for bars, exchanges, units, and currencies.
"""

from typing import Optional, List, Dict
from .TVTypes import ResolutionString, SessionId


class TVBar:
    """
    Bar data point representing OHLCV data for a specific time period.
    
    Attributes:
        time: Bar time in milliseconds since Unix epoch in UTC timezone.
              For daily, weekly, and monthly bars, time is expected to be
              a trading day (not session start day) at 00:00 UTC.
        open: Opening price
        high: High price
        low: Low price
        close: Closing price
        volume: Trading volume (optional)
    """
    def __init__(
        self,
        time: int,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: Optional[float] = None
    ):
        self.time = time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def to_dict(self) -> dict:
        """Convert bar data to dictionary format."""
        return {
            "time": self.time,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume
        }


class TVHistoryMetadata:
    """
    Metadata information passed to onHistoryCallback for getBars.
    
    Attributes:
        noData: Optional flag indicating no more data is available on the server
        nextTime: Time of the next available bar in history (Unix timestamp in milliseconds)
    """
    def __init__(
        self,
        noData: Optional[bool] = None,
        nextTime: Optional[int] = None
    ):
        self.noData = noData
        self.nextTime = nextTime


class TVExchange:
    """
    Exchange descriptor containing exchange information.
    
    Attributes:
        value: Value to be passed as the 'exchange' argument to searchSymbols
        name: Display name of the exchange
        desc: Description of the exchange
    """
    def __init__(self, value: str, name: str, desc: str):
        self.value = value
        self.name = name
        self.desc = desc


class TVDatafeedSymbolType:
    """
    Symbol type descriptor for filtering in symbol search.
    
    Attributes:
        name: Display name of the symbol type
        value: Value to be passed as the 'symbolType' argument to searchSymbols
    """
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


class TVUnit:
    """
    Unit definition for unit conversion.
    
    Attributes:
        id: Unique identifier for the unit
        name: Short name of the unit
        description: Detailed description of the unit
    """
    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description


class TVCurrencyItem:
    """
    Currency item for currency conversion.
    
    Attributes:
        id: Unique identifier for the currency
        code: Currency code (e.g., "USD", "EUR")
        logoUrl: Optional URL to currency logo image (SVG preferred, 24x24px for raster)
        description: Optional description of the currency
    """
    def __init__(
        self,
        id: str,
        code: str,
        logoUrl: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.id = id
        self.code = code
        self.logoUrl = logoUrl
        self.description = description


class TVDatafeedConfiguration:
    """
    Datafeed configuration data passed to onReady callback.
    
    This configuration defines the capabilities and options supported
    by the datafeed implementation.
    """
    def __init__(
        self,
        exchanges: Optional[List[TVExchange]] = None,
        supported_resolutions: Optional[List[ResolutionString]] = None,
        units: Optional[Dict[str, List[TVUnit]]] = None,
        currency_codes: Optional[List] = None,
        supports_marks: Optional[bool] = None,
        supports_time: Optional[bool] = None,
        supports_timescale_marks: Optional[bool] = None,
        symbols_types: Optional[List[TVDatafeedSymbolType]] = None,
        symbols_grouping: Optional[Dict[str, str]] = None
    ):
        self.exchanges = exchanges or []
        self.supported_resolutions = supported_resolutions
        self.units = units
        self.currency_codes = currency_codes
        self.supports_marks = supports_marks
        self.supports_time = supports_time
        self.supports_timescale_marks = supports_timescale_marks
        self.symbols_types = symbols_types
        self.symbols_grouping = symbols_grouping


class TVPeriodParams:
    """
    Parameters passed to getBars method for requesting historical data.
    
    Attributes:
        from_: Unix timestamp of the leftmost requested bar
        to: Unix timestamp of the rightmost requested bar (not inclusive)
        countBack: Exact amount of bars to load (higher priority than 'from_' if supported)
        firstDataRequest: Flag indicating if this is the first call of getBars
    """
    def __init__(
        self,
        from_: int,
        to: int,
        countBack: int,
        firstDataRequest: bool
    ):
        self.from_ = from_
        self.to = to
        self.countBack = countBack
        self.firstDataRequest = firstDataRequest


class TVDOMLevel:
    """
    Depth of Market (Order Book) level data.
    
    Attributes:
        price: Price for this DOM level
        volume: Volume at this price level
    """
    def __init__(self, price: float, volume: float):
        self.price = price
        self.volume = volume


class TVDOMData:
    """
    Depth of Market (Order Book) data.
    
    Attributes:
        snapshot: True if data contains full depth, False if only updated levels
        asks: Ask order levels (sorted by price in ascending order)
        bids: Bid order levels (sorted by price in ascending order)
    """
    def __init__(
        self,
        snapshot: bool,
        asks: List[TVDOMLevel],
        bids: List[TVDOMLevel]
    ):
        self.snapshot = snapshot
        self.asks = asks
        self.bids = bids


__all__ = [
    "TVBar",
    "TVHistoryMetadata",
    "TVExchange",
    "TVDatafeedSymbolType",
    "TVUnit",
    "TVCurrencyItem",
    "TVDatafeedConfiguration",
    "TVPeriodParams",
    "TVDOMLevel",
    "TVDOMData",
]
