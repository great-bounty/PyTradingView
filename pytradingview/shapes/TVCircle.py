from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVCircleOverrides(TVBaseOverrides):

    def __init__(self):
        # Default value: `rgba(255, 152, 0, 0.2)`
        self.backgroundColor = "rgba(255, 152, 0, 0.2)"
        
        # Default value: `false`
        self.bold = False
        
        # Default value: `#FF9800`
        self.color = "#FF9800"
        
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
        
        # Default value: `#FF9800`
        self.textColor = "#FF9800"

class TVCircle(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVCircleOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Circle
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
