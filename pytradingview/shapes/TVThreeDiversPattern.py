from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVThreeDiversPatternOverrides(TVBaseOverrides):

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

class TVThreeDiversPattern(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVThreeDiversPatternOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.ThreeDiversPattern
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
