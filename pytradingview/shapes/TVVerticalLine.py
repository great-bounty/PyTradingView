from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVVerticalLineOverrides(TVBaseOverrides):
    
    def __init__(self):
        self.bold = False
        self.extendLine = True
        self.fontsize = 14
        self.horzLabelsAlign = "center"
        self.italic = False
        self.linecolor = "#2962FF"
        self.linestyle = 0
        self.linewidth = 2
        self.showLabel = False
        self.showTime = True
        self.textcolor = "#2962FF"
        self.textOrientation = "vertical"
        self.vertLabelsAlign = "middle"

class TVVerticalLine(TVSingleShape):

    def __init__(self, overrides: Optional[TVVerticalLineOverrides] = None, **kwargs):
        shape = TVSingleShapeType.VerticalLine
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
