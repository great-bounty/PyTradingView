from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVArrowMarkerOverrides(TVBaseOverrides):
    
    def __init__(self) -> None:
        self.backgroundColor: str = "#1E53E5"
        self.bold: bool = True
        self.fontsize: int = 16
        self.italic: bool = False
        self.showLabel: bool = True
        self.textColor: str = "#1E53E5"

class TVArrowMarker(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVArrowMarkerOverrides] = None, **kwargs):
        shape = TVSingleShapeType.ArrowMarker
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
