from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVTrianglePatternOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "#673ab7"
        self.bold = False
        self.color = "#673ab7"
        self.fill_background = True
        self.font_size = 12
        self.italic = False
        self.line_width = 2
        self.text_color = "#ffffff"
        self.transparency = 85

class TVTrianglePattern(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVTrianglePatternOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.TrianglePattern
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
