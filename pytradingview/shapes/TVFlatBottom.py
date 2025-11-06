from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVFlatBottomOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "rgba(255, 152, 0, 0.2)"
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
        self.label_text_color = "#FF9800"
        self.label_vert_align = "bottom"
        self.label_visible = False
        self.left_end = 0
        self.line_color = "#FF9800"
        self.line_style = 0
        self.line_width = 2
        self.right_end = 0
        self.show_bars_range = False
        self.show_date_time_range = False
        self.show_price_range = False
        self.show_prices = False
        self.text_color = "#FF9800"
        self.transparency = 20

class TVFlatBottom(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVFlatBottomOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.FlatBottom
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)