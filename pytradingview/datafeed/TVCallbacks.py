"""
TradingView Datafeed Callback Type Definitions
Type aliases for all callback functions used in the datafeed API.
"""

from typing import Callable, List, Optional, Union

# Forward declarations for type hints
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .TVDataStructures import (
        TVBar,
        TVHistoryMetadata,
        TVDatafeedConfiguration,
        TVDOMData,
    )
    from .TVSymbolInfo import (
        TVLibrarySymbolInfo,
        TVSearchSymbolResultItem,
    )
    from .TVMarks import TVMark, TVTimescaleMark
    from .TVQuotes import TVQuoteData


# Configuration callback
TVOnReadyCallback = Callable[['TVDatafeedConfiguration'], None]

# Symbol search callbacks
TVSearchSymbolsCallback = Callable[[List['TVSearchSymbolResultItem']], None]
TVResolveCallback = Callable[['TVLibrarySymbolInfo'], None]

# Error callback
TVDatafeedErrorCallback = Callable[[str], None]

# History data callbacks
TVHistoryCallback = Callable[[List['TVBar'], Optional['TVHistoryMetadata']], None]

# Real-time bar updates
TVSubscribeBarsCallback = Callable[['TVBar'], None]

# Marks callbacks
TVGetMarksCallback = Callable[[List[Union['TVMark', 'TVTimescaleMark']]], None]

# Server time callback
TVServerTimeCallback = Callable[[int], None]

# Depth of Market callback
TVDOMCallback = Callable[['TVDOMData'], None]

# Quotes callbacks
TVQuotesCallback = Callable[[List['TVQuoteData']], None]
TVQuotesErrorCallback = Callable[[str], None]


__all__ = [
    "TVOnReadyCallback",
    "TVSearchSymbolsCallback",
    "TVResolveCallback",
    "TVDatafeedErrorCallback",
    "TVHistoryCallback",
    "TVSubscribeBarsCallback",
    "TVGetMarksCallback",
    "TVServerTimeCallback",
    "TVDOMCallback",
    "TVQuotesCallback",
    "TVQuotesErrorCallback",
]
