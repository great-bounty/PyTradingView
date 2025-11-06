from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVEllipseOverrides(TVBaseOverrides):
    
    def __init__(self):
        # Default value: `rgba(242, 54, 69, 0.2)`
        self.backgroundColor = "rgba(242, 54, 69, 0.2)"
        
        # Default value: `false`
        self.bold = False
        
        # Default value: `#F23645`
        self.color = "#F23645"
        
        # Default value: `true`
        self.fillBackground = True
        
        # Default value: `14`
        self.fontSize = 14
        
        # Default value: `false`
        self.italic = False
        
        # Default value: `2`
        self.linewidth = 2
        
        # Default value: `false`
        self.showLabel = False
        
        # Default value: `#F23645`
        self.textColor = "#F23645"
        
        # Default value: `50`
        self.transparency = 50

class TVEllipse(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVEllipseOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Ellipse
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
