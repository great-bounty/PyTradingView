from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVDisjointAngleOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "rgba(8, 153, 129, 0.2)"
        self.bold = False
        self.extend_left = False
        self.extend_right = False
        self.fill_background = True
        self.font_size = 12
        self.italic = False
        self.label_bold = False
        self.label_font_size = 14
        self.label_horz_align = "left"
        self.label_italic = False
        self.label_text_color = "#089981"
        self.label_vert_align = "bottom"
        self.label_visible = False
        self.left_end = 0
        self.line_color = "#089981"
        self.line_style = 0
        self.line_width = 2
        self.right_end = 0
        self.show_bars_range = False
        self.show_date_time_range = False
        self.show_price_range = False
        self.show_prices = False
        self.text_color = "#089981"
        self.transparency = 20

class TVDisjointAngle(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVDisjointAngleOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.DisjointAngle
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)