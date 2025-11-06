from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVSineLineOverrides(TVBaseOverrides):

    def __init__(self):
        self.linecolor = "#159980"
        self.linestyle = 0
        self.linewidth = 2

class TVSineLine(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVSineLineOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.SineLine
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
