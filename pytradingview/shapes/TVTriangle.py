from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVTriangleOverrides(TVBaseOverrides):

    def __init__(self):
        # Default value: `rgba(8, 153, 129, 0.2)`
        self.backgroundColor = "rgba(8, 153, 129, 0.2)"
        
        # Default value: `#089981`
        self.color = "#089981"
        
        # Default value: `true`
        self.fillBackground = True
        
        # Default value: `2`
        self.linewidth = 2
        
        # Default value: `80`
        self.transparency = 80

class TVTriangle(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVTriangleOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Triangle
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
