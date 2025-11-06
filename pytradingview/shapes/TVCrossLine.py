from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVCrossLineOverrides(TVBaseOverrides):

    def __init__(self):
        self.line_color = "#2962FF"
        self.line_style = 0
        self.line_width = 2
        self.show_price = True
        self.show_time = True

class TVCrossLine(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVCrossLineOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.CrossLine
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)