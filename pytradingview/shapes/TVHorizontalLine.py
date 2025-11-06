from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVHorizontalLineOverrides(TVBaseOverrides):

    def __init__(self):
        self.bold: bool = False
        self.fontsize: int = 12
        self.horzLabelsAlign: str = "center"
        self.italic: bool = False
        self.linecolor: str = "#2962FF"
        self.linestyle: int = 0
        self.linewidth: int = 2
        self.showLabel: bool = False
        self.showPrice: bool = True
        self.textcolor: str = "#2962FF"
        self.vertLabelsAlign: str = "middle"

class TVHorizontalLine(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVHorizontalLineOverrides] = None, **kwargs):
        shape = TVSingleShapeType.HorizontalLine
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
