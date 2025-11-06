"""
BADatafeed Implementation Example

Demonstrates how to inherit and implement a custom Datafeed.
"""

from typing import List, Optional
from .TVDatafeed import TVDatafeed
from .TVDataStructures import (
    TVDatafeedConfiguration, TVExchange, TVBar,
    TVPeriodParams, TVHistoryMetadata
)
from .TVSymbolInfo import (
    TVLibrarySymbolInfo, TVSearchSymbolResultItem, TVSymbolResolveExtension
)
from .TVCallbacks import (
    TVOnReadyCallback, TVSearchSymbolsCallback, TVResolveCallback,
    TVDatafeedErrorCallback, TVHistoryCallback, TVSubscribeBarsCallback
)
from .TVTypes import ResolutionString
import logging

logger = logging.getLogger(__name__)


class BADatafeed(TVDatafeed):
    """
    Custom Datafeed Implementation Example
    Inherits from TVDatafeed and implements specific data retrieval logic.
    """

    def __init__(self):
        super().__init__()
        # Configure data source
        self._configuration = TVDatafeedConfiguration(
            exchanges=[
                TVExchange(value="BINANCE", name="Binance", desc="Binance Exchange"),
                TVExchange(value="OKEX", name="OKEx", desc="OKEx Exchange")
            ],
            supported_resolutions=["1", "5", "15", "30", "60", "240", "1D", "1W", "1M"],
            supports_marks=False,
            supports_time=True,
            supports_timescale_marks=False
        )

    def onReady(self, callback: TVOnReadyCallback) -> None:
        """Returns configuration information."""
        if self._configuration is not None:
            callback(self._configuration)

    def searchSymbols(
        self,
        userInput: str,
        exchange: str,
        symbolType: str,
        onResult: TVSearchSymbolsCallback
    ) -> None:
        """Search for symbols."""
        # Mock search results
        results = []
        if "BTC" in userInput.upper():
            results.append(TVSearchSymbolResultItem(
                symbol="BTCUSDT",
                description="Bitcoin / Tether",
                exchange="BINANCE",
                type="crypto",
                ticker="BTCUSDT"
            ))
        if "ETH" in userInput.upper():
            results.append(TVSearchSymbolResultItem(
                symbol="ETHUSDT",
                description="Ethereum / Tether",
                exchange="BINANCE",
                type="crypto",
                ticker="ETHUSDT"
            ))
        onResult(results)

    def resolveSymbol(
        self,
        symbolName: str,
        onResolve: TVResolveCallback,
        onError: TVDatafeedErrorCallback,
        extension: Optional[TVSymbolResolveExtension] = None
    ) -> None:
        """Resolve symbol information."""
        try:
            # Construct symbol information
            symbol_info = TVLibrarySymbolInfo(
                name=symbolName,
                ticker=symbolName,
                description=f"{symbolName} Description",
                type="crypto",
                session="24x7",
                exchange="BINANCE",
                listed_exchange="BINANCE",
                timezone="Etc/UTC",
                format="price",
                pricescale=100,
                minmov=1,
                has_intraday=True,
                has_daily=True,
                supported_resolutions=["1", "5", "15", "30", "60", "1D"],
                volume_precision=2
            )
            onResolve(symbol_info)
        except Exception as e:
            logger.error(f"Error resolving symbol: {e}")
            onError(str(e))

    def getBars(
        self,
        symbolInfo: TVLibrarySymbolInfo,
        resolution: ResolutionString,
        periodParams: TVPeriodParams,
        onResult: TVHistoryCallback,
        onError: TVDatafeedErrorCallback
    ) -> None:
        """Get historical bar data."""
        try:
            # Should retrieve bar data from actual data source
            # Example returns empty data
            bars: List[TVBar] = []
            
            # Example: Create some mock data
            # for i in range(10):
            #     bars.append(TVBar(
            #         time=periodParams.from_ + i * 60000,
            #         open=100.0 + i,
            #         high=105.0 + i,
            #         low=95.0 + i,
            #         close=102.0 + i,
            #         volume=1000.0
            #     ))
            
            metadata = TVHistoryMetadata(noData=len(bars) == 0)
            onResult(bars, metadata)
            
        except Exception as e:
            logger.error(f"Error getting bars: {e}")
            onError(str(e))

    def subscribeBars(
        self,
        symbolInfo: TVLibrarySymbolInfo,
        resolution: ResolutionString,
        onTick: TVSubscribeBarsCallback,
        listenerGuid: str,
        onResetCacheNeededCallback
    ) -> None:
        """Subscribe to real-time bars."""
        super().subscribeBars(
            symbolInfo,
            resolution,
            onTick,
            listenerGuid,
            onResetCacheNeededCallback
        )
        
        # Should start WebSocket or other real-time data subscription
        logger.info(f"Starting real-time subscription for {symbolInfo.name} @ {resolution}")
        
        # Example: Mock pushing real-time data
        # In actual application, this should be called in WebSocket callback
        # new_bar = TVBar(
        #     time=int(time.time() * 1000),
        #     open=100.0,
        #     high=105.0,
        #     low=95.0,
        #     close=102.0,
        #     volume=1000.0
        # )
        # onTick(new_bar)


# ========== Usage Example ==========

def main():
    """Main function example."""
    logging.basicConfig(level=logging.INFO)
    
    # Create datafeed instance
    datafeed = BADatafeed()
    
    # Test configuration retrieval
    def on_ready_callback(config: TVDatafeedConfiguration):
        print(f"Configuration ready, supported resolutions: {config.supported_resolutions}")
        print(f"Exchange list: {[ex.name for ex in config.exchanges]}")
    
    datafeed.onReady(on_ready_callback)
    
    # Test search
    def on_search_result(results: List[TVSearchSymbolResultItem]):
        print(f"\nSearch results:")
        for item in results:
            print(f"  {item.symbol} - {item.description} ({item.exchange})")
    
    datafeed.searchSymbols("BTC", "", "", on_search_result)
    
    # Test symbol resolution
    def on_resolve(symbol_info: TVLibrarySymbolInfo):
        print(f"\nSymbol information:")
        print(f"  Name: {symbol_info.name}")
        print(f"  Description: {symbol_info.description}")
        print(f"  Type: {symbol_info.type}")
        print(f"  Exchange: {symbol_info.exchange}")
    
    def on_error(error: str):
        print(f"Error: {error}")
    
    datafeed.resolveSymbol("BTCUSDT", on_resolve, on_error)


if __name__ == "__main__":
    main()
