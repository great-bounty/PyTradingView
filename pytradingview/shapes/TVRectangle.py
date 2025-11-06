from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVRectangleOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.backgroundColor: str = "rgba(156, 39, 176, 0.2)"
        self.bold: bool = False
        self.color: str = "#9c27b0"
        self.extendLeft: bool = False
        self.extendRight: bool = False
        self.fillBackground: bool = True
        self.fontSize: int = 14
        self.horzLabelsAlign: str = "center"
        self.italic: bool = False
        self.linewidth: int = 2
        self.middleLineLineColor: str = "#9c27b0"
        self.middleLineLineStyle: int = 2
        self.middleLineLineWidth: int = 1
        self.middleLineShowLine: bool = False
        self.showLabel: bool = False
        self.textColor: str = "#9c27b0"
        self.transparency: int = 50
        self.vertLabelsAlign: str = "middle"

class TVRectangle(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVRectangleOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Rectangle
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
