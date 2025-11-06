from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVBalloonOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.background_color: str = "rgba(156, 39, 176, 0.7)"
        self.border_color: str = "rgba(156, 39, 176, 0)"
        self.color: str = "#ffffff"
        self.fontsize: int = 14
        self.transparency: int = 30

class TVBalloon(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVBalloonOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Balloon
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
