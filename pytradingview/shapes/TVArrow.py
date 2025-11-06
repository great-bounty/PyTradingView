from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVArrowOverrides(TVBaseOverrides):

    def __init__(self):
        self.always_show_stats = False
        self.bold = False
        self.extend_left = False
        self.extend_right = False
        self.font_size = 14
        self.horz_labels_align = "center"
        self.italic = False
        self.left_end = 0
        self.line_color = "#2962FF"
        self.line_style = 0
        self.line_width = 2
        self.right_end = 1
        self.show_angle = False
        self.show_bars_range = False
        self.show_date_time_range = False
        self.show_distance = False
        self.show_label = False
        self.show_middle_point = False
        self.show_percent_price_range = False
        self.show_pips_price_range = False
        self.show_price_labels = False
        self.show_price_range = False
        self.stats_position = 2
        self.text_color = "#2962FF"
        self.vert_labels_align = "bottom"

class TVArrow(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVArrowOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Arrow
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)