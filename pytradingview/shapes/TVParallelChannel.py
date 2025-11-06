from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVParallelChannelOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "rgba(41, 98, 255, 0.2)"
        self.extend_left = False
        self.extend_right = False
        self.fill_background = True
        self.label_bold = False
        self.label_font_size = 14
        self.label_horz_align = "left"
        self.label_italic = False
        self.label_text_color = "#2962FF"
        self.label_vert_align = "bottom"
        self.label_visible = False
        self.line_color = "#2962FF"
        self.line_style = 0
        self.line_width = 2
        self.midline_color = "#2962FF"
        self.midline_style = 2
        self.midline_width = 1
        self.show_midline = True
        self.transparency = 20

class TVParallelChannel(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVParallelChannelOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.ParallelChannel
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)