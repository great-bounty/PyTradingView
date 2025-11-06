from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVDateAndPriceRangeOverrides(TVBaseOverrides):

    def __init__(self):
        self.backgroundColor = "#2962FF"
        self.borderColor = "#2962FF"
        self.color = "#ffffff"
        self.fontsize = 14
        self.fontWeight = "bold"
        self.transparency = 0

class TVDateAndPriceRange(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVDateAndPriceRangeOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.DateAndPriceRange
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
