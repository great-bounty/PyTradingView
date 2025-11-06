from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVBarsPatternOverrides(TVBaseOverrides):

    def __init__(self):
        self.color = "#2962FF"
        self.flipped = False
        self.mirrored = False
        self.mode = 0

class TVBarsPattern(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVBarsPatternOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.BarsPattern
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
