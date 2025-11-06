from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVTrendAngleOverrides(TVBaseOverrides):

    def __init__(self):
        self.always_show_stats = False
        self.bold = False
        self.extend_left = False
        self.extend_right = False
        self.font_size = 12
        self.italic = False
        self.line_color = "#2962FF"
        self.line_style = 0
        self.line_width = 2
        self.show_bars_range = False
        self.show_middle_point = False
        self.show_percent_price_range = False
        self.show_pips_price_range = False
        self.show_price_labels = False
        self.show_price_range = False
        self.stats_position = 2

class TVTrendAngle(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVTrendAngleOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.TrendAngle
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)