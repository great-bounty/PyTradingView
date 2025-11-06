from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVArrowLeftOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.arrowColor: str = "#2962FF"
        self.bold: bool = False
        self.color: str = "#2962FF"
        self.fontsize: int = 14
        self.italic: bool = False
        self.showLabel: bool = True

class TVArrowLeft(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVArrowLeftOverrides] = None, **kwargs):
        shape = TVSingleShapeType.ArrowLeft
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
