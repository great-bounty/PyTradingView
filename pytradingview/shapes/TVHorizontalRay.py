from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVHorizontalRayOverrides(TVBaseOverrides):

    def __init__(self):
        self.bold = False
        self.font_size = 12
        self.horz_labels_align = "center"
        self.italic = False
        self.line_color = "#2962FF"
        self.line_style = 0
        self.line_width = 2
        self.show_label = False
        self.show_price = True
        self.text_color = "#2962FF"
        self.vert_labels_align = "top"

class TVHorizontalRay(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVHorizontalRayOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.HorizontalRay
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)