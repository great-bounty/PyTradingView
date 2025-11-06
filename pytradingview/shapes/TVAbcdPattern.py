from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVAbcdPatternOverrides(TVBaseOverrides):

    def __init__(self):
        self.bold = False
        self.color = "#089981"
        self.font_size = 12
        self.italic = False
        self.line_width = 2
        self.text_color = "#ffffff"

class TVAbcdPattern(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVAbcdPatternOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.AbcdPattern
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
