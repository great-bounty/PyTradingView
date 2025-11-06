from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVDateRangeOverrides(TVBaseOverrides):

    def __init__(self):
        self.linecolor = "#159980"
        self.linestyle = 0
        self.linewidth = 2

class TVDateRange(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVDateRangeOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.DateRange
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
