from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVRotatedRectangleOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "rgba(76, 175, 80, 0.2)"
        self.color = "#4caf50"
        self.fill_background = True
        self.linewidth = 2
        self.transparency = 50

class TVRotatedRectangle(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVRotatedRectangleOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.RotatedRectangle
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
