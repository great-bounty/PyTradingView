from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVArcOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "rgba(233, 30, 99, 0.2)"
        self.color = "#e91e63"
        self.fill_background = True
        self.linewidth = 2
        self.transparency = 80

class TVArc(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVArcOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Arc
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
