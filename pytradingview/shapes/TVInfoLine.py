from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVInfoLineOverrides(TVBaseOverrides):

    def __init__(self):
        self.always_show_stats = True
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
        self.right_end = 0
        self.show_angle = True
        self.show_bars_range = True
        self.show_date_time_range = True
        self.show_distance = True
        self.show_label = False
        self.show_middle_point = False
        self.show_percent_price_range = True
        self.show_pips_price_range = True
        self.show_price_labels = False
        self.show_price_range = True
        self.stats_position = 1
        self.text_color = "#2962FF"
        self.vert_labels_align = "bottom"

class TVInfoLine(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVInfoLineOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.InfoLine
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)