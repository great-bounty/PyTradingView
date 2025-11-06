from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVArrowDownOverrides(TVBaseOverrides):

    def __init__(self):
        self.arrowColor = "#CC2F3C"
        self.bold = False
        self.color = "#CC2F3C"
        self.fontsize = 14
        self.italic = False
        self.showLabel = True

class TVArrowDown(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVArrowDownOverrides] = None, **kwargs):
        shape = TVSingleShapeType.ArrowDown
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
