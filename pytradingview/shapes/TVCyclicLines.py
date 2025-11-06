from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVCyclicLinesOverrides(TVBaseOverrides):

    def __init__(self):
        self.backgroundColor = "rgba(106, 168, 79, 0.5)"
        self.fillBackground = True
        self.linecolor = "#159980"
        self.linestyle = 0
        self.linewidth = 2
        self.transparency = 50

class TVCyclicLines(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVCyclicLinesOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.CyclicLines
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
