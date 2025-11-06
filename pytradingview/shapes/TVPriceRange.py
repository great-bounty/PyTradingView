from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVPriceRangeOverrides(TVBaseOverrides):

    def __init__(self):
        self.backgroundColor = "#2962FF"
        self.borderColor = "#2962FF"
        self.color = "#ffffff"
        self.fontsize = 14
        self.fontWeight = "bold"
        self.transparency = 0

class TVPriceRange(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVPriceRangeOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.PriceRange
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
