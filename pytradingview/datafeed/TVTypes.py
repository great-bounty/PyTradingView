"""
TradingView Datafeed Type Definitions
Type aliases and literal types used across the datafeed API.
"""

from typing import Literal

# Resolution string for different time intervals
# Examples: "1" (1 minute), "5" (5 minutes), "1D" (1 day), "1W" (1 week), "1M" (1 month)
ResolutionString = str

# Timezone identifier in OlsonDB format
# Examples: "Etc/UTC", "America/New_York", "Asia/Shanghai"
Timezone = str

# Format for displaying labels on the price scale
SeriesFormat = Literal["price", "volume"]

# Set of plots visible on the chart
VisiblePlotsSet = Literal["ohlcv", "ohlc", "c"]

# Data status indicating streaming type
DataStatus = Literal["streaming", "endofday", "delayed_streaming"]

# Session identifier for different trading periods
SessionId = Literal["regular", "extended", "premarket", "postmarket"]

# Status code for quote data response
QuoteStatus = Literal["ok", "error"]

# Mark color constants
MarkColor = Literal["red", "green", "blue", "yellow"]

# Timescale mark shape types
TimeScaleMarkShape = Literal["circle", "earningUp", "earningDown", "earning"]

# Symbol type for filtering
SymbolType = str

__all__ = [
    "ResolutionString",
    "Timezone",
    "SeriesFormat",
    "VisiblePlotsSet",
    "DataStatus",
    "SessionId",
    "QuoteStatus",
    "MarkColor",
    "TimeScaleMarkShape",
    "SymbolType",
]
