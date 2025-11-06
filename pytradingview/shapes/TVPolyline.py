from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVPolylineOverrides(TVBaseOverrides):

    def __init__(self):
        # Default value: `rgba(0, 188, 212, 0.2)`
        self.backgroundColor = "rgba(0, 188, 212, 0.2)"
        
        # Default value: `true`
        self.fillBackground = True
        
        # Default value: `false`
        self.filled = False
        
        # Default value: `#00bcd4`
        self.linecolor = "#00bcd4"
        
        # Default value: `0`
        self.linestyle = 0
        
        # Default value: `2`
        self.linewidth = 2
        
        # Default value: `80`
        self.transparency = 80

class TVPolyline(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVPolylineOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Polyline
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
