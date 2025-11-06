from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVGhostFeedOverrides(TVBaseOverrides):

    def __init__(self):
        self.average_hl = 20
        self.candle_style_border_color = "#378658"
        self.candle_style_border_down_color = "#F23645"
        self.candle_style_border_up_color = "#089981"
        self.candle_style_down_color = "#FAA1A4"
        self.candle_style_draw_border = True
        self.candle_style_draw_wick = True
        self.candle_style_up_color = "#ACE5DC"
        self.candle_style_wick_color = "#787B86"
        self.transparency = 50
        self.variance = 50

class TVGhostFeed(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVGhostFeedOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.GhostFeed
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
