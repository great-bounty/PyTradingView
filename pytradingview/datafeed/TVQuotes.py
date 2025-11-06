"""
TradingView Quote Data Structures
Structures for real-time quote data and responses.
"""

from typing import Union, Optional, Any
from .TVTypes import QuoteStatus


class TVDatafeedQuoteValues:
    """
    Symbol quote values containing current price data.
    
    This object contains quote values describing the current price state.
    Used for trading functionalities including Order Ticket, Legend,
    Watchlist, Details, News, and Depth of Market widgets.
    
    All properties are optional, but most should be populated for
    proper trading functionality support.
    
    Attributes:
        ch: Price change (usually from open price on the day)
        chp: Price change percentage
        short_name: Short symbol name for widget titles
        exchange: Exchange name
        description: Short symbol description
        lp: Last price (most recent trade price)
        ask: Ask price
        bid: Bid price
        spread: Spread (difference between ask and bid)
        open_price: Today's opening price
        high_price: Today's high price
        low_price: Today's low price
        prev_close_price: Previous session's closing price
        volume: Today's trading volume
        original_name: Original symbol name
    """
    def __init__(self, **kwargs):
        self.ch = kwargs.get('ch')
        self.chp = kwargs.get('chp')
        self.short_name = kwargs.get('short_name')
        self.exchange = kwargs.get('exchange')
        self.description = kwargs.get('description')
        self.lp = kwargs.get('lp')
        self.ask = kwargs.get('ask')
        self.bid = kwargs.get('bid')
        self.spread = kwargs.get('spread')
        self.open_price = kwargs.get('open_price')
        self.high_price = kwargs.get('high_price')
        self.low_price = kwargs.get('low_price')
        self.prev_close_price = kwargs.get('prev_close_price')
        self.volume = kwargs.get('volume')
        self.original_name = kwargs.get('original_name')


class TVQuoteData:
    """
    Quote data response structure.
    
    This class represents the response structure for quote data requests,
    which can be either successful ("ok") or error responses.
    
    Attributes:
        s: Status code ("ok" or "error")
        n: Symbol name (must match the request exactly)
        v: Quote values (TVDatafeedQuoteValues for "ok", dict for "error")
    """
    def __init__(
        self,
        s: QuoteStatus,
        n: str,
        v: Union[TVDatafeedQuoteValues, dict]
    ):
        self.s = s
        self.n = n
        self.v = v


__all__ = [
    "TVDatafeedQuoteValues",
    "TVQuoteData",
]
