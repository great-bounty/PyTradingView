"""
TradingView Symbol Information Structures
Symbol-related data structures including symbol info and search results.
"""

from typing import Optional, List, Dict, Any
from .TVTypes import (
    Timezone,
    SeriesFormat,
    VisiblePlotsSet,
    DataStatus,
    SessionId,
    ResolutionString
)


class TVSymbolInfoPriceSource:
    """
    Symbol price source information.
    
    Price sources indicate the origin of values represented by symbol bars.
    Examples: "Spot Price", "Ask", "Bid", etc.
    
    Attributes:
        id: Unique identifier for the price source
        name: Display name of the price source
    """
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class TVLibrarySubsessionInfo:
    """
    Subsession information for extended trading sessions.
    
    Attributes:
        description: Description of the subsession (e.g., "Regular Trading Hours")
        id: Subsession identifier
        session: Session string defining trading hours
        session_correction: Optional session corrections string
        session_display: Optional session display string
    """
    def __init__(
        self,
        description: str,
        id: SessionId,
        session: str,
        session_correction: Optional[str] = None,
        session_display: Optional[str] = None
    ):
        self.description = description
        self.id = id
        self.session = session
        self.session_correction = session_correction
        self.session_display = session_display


class TVLibrarySymbolInfo:
    """
    Complete symbol information used by the TradingView library.
    
    This class contains all metadata about a trading symbol including
    its exchange, timezone, trading sessions, price format, and capabilities.
    
    Required parameters:
        name: Symbol name within exchange (e.g., "AAPL", "9988")
        description: Symbol description displayed in chart legend
        type: Instrument type (stock, futures, forex, index, etc.)
        session: Trading hours in exchange timezone
        exchange: Traded exchange (current/proxy exchange)
        listed_exchange: Real exchange where symbol is listed
        timezone: Exchange timezone in OlsonDB format
        format: Price scale label format ("price" or "volume")
        pricescale: Decimal places (10^n) or fractions (2^n)
        minmov: Minimum price movement units
    """
    def __init__(
        self,
        name: str,
        description: str,
        type: str,
        session: str,
        exchange: str,
        listed_exchange: str,
        timezone: Timezone,
        format: SeriesFormat,
        pricescale: int,
        minmov: int,
        **kwargs
    ):
        # Required fields
        self.name = name
        self.description = description
        self.type = type
        self.session = session
        self.exchange = exchange
        self.listed_exchange = listed_exchange
        self.timezone = timezone
        self.format = format
        self.pricescale = pricescale
        self.minmov = minmov
        
        # Optional identifier fields
        self.ticker = kwargs.get('ticker')
        self.base_name = kwargs.get('base_name')
        self.long_description = kwargs.get('long_description')
        
        # Session configuration
        self.session_display = kwargs.get('session_display')
        self.session_holidays = kwargs.get('session_holidays')
        self.corrections = kwargs.get('corrections')
        
        # Price format configuration
        self.fractional = kwargs.get('fractional', False)
        self.minmove2 = kwargs.get('minmove2', 0)
        self.variable_tick_size = kwargs.get('variable_tick_size')
        
        # Resolution support
        self.has_intraday = kwargs.get('has_intraday', False)
        self.supported_resolutions = kwargs.get('supported_resolutions')
        self.intraday_multipliers = kwargs.get('intraday_multipliers', [])
        self.has_seconds = kwargs.get('has_seconds', False)
        self.has_ticks = kwargs.get('has_ticks', False)
        self.seconds_multipliers = kwargs.get('seconds_multipliers')
        self.build_seconds_from_ticks = kwargs.get('build_seconds_from_ticks', False)
        self.has_daily = kwargs.get('has_daily', True)
        self.daily_multipliers = kwargs.get('daily_multipliers', ['1'])
        self.has_weekly_and_monthly = kwargs.get('has_weekly_and_monthly', False)
        self.weekly_multipliers = kwargs.get('weekly_multipliers', ['1'])
        self.monthly_multipliers = kwargs.get('monthly_multipliers', ['1'])
        
        # Display configuration
        self.has_empty_bars = kwargs.get('has_empty_bars', False)
        self.visible_plots_set = kwargs.get('visible_plots_set', 'ohlcv')
        self.volume_precision = kwargs.get('volume_precision', 0)
        
        # Data status and timing
        self.data_status = kwargs.get('data_status')
        self.delay = kwargs.get('delay')
        self.expired = kwargs.get('expired', False)
        self.expiration_date = kwargs.get('expiration_date')
        
        # Classification
        self.sector = kwargs.get('sector')
        self.industry = kwargs.get('industry')
        
        # Currency and unit conversion
        self.currency_code = kwargs.get('currency_code')
        self.original_currency_code = kwargs.get('original_currency_code')
        self.unit_id = kwargs.get('unit_id')
        self.original_unit_id = kwargs.get('original_unit_id')
        self.unit_conversion_types = kwargs.get('unit_conversion_types')
        
        # Extended sessions
        self.subsession_id = kwargs.get('subsession_id')
        self.subsessions = kwargs.get('subsessions')
        
        # Price sources
        self.price_source_id = kwargs.get('price_source_id')
        self.price_sources = kwargs.get('price_sources')
        
        # Logos
        self.logo_urls = kwargs.get('logo_urls')
        self.exchange_logo = kwargs.get('exchange_logo')
        
        # Custom metadata
        self.library_custom_fields = kwargs.get('library_custom_fields')


class TVSearchSymbolResultItem:
    """
    Symbol search result item.
    
    Represents a single symbol in the search results list.
    
    Attributes:
        symbol: Short symbol name
        description: Symbol description
        exchange: Exchange name
        type: Symbol type (stock, futures, forex, index, etc.)
        ticker: Optional unique symbol identifier
        logo_urls: Optional list of 1-2 logo URLs (2 for overlapping circles, e.g., forex pairs)
        exchange_logo: Optional exchange logo URL
    """
    def __init__(
        self,
        symbol: str,
        description: str,
        exchange: str,
        type: str,
        ticker: Optional[str] = None,
        logo_urls: Optional[List[str]] = None,
        exchange_logo: Optional[str] = None
    ):
        self.symbol = symbol
        self.description = description
        self.exchange = exchange
        self.type = type
        self.ticker = ticker
        self.logo_urls = logo_urls
        self.exchange_logo = exchange_logo


class TVSymbolResolveExtension:
    """
    Additional information for symbol resolution.
    
    This extension provides context for currency/unit conversion
    and session selection during symbol resolution.
    
    Attributes:
        currencyCode: Currency code for conversion if supported
        unitId: Unit identifier for conversion if supported
        session: Trading session type (e.g., "regular", "extended")
    """
    def __init__(
        self,
        currencyCode: Optional[str] = None,
        unitId: Optional[str] = None,
        session: Optional[str] = None
    ):
        self.currencyCode = currencyCode
        self.unitId = unitId
        self.session = session


__all__ = [
    "TVSymbolInfoPriceSource",
    "TVLibrarySubsessionInfo",
    "TVLibrarySymbolInfo",
    "TVSearchSymbolResultItem",
    "TVSymbolResolveExtension",
]
