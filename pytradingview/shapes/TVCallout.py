from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVCalloutOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.background_color: str = "rgba(0, 151, 167, 0.7)"
        self.bold: bool = False
        self.bordercolor: str = "#0097A7"
        self.color: str = "#ffffff"
        self.fontsize: int = 14
        self.italic: bool = False
        self.linewidth: int = 2
        self.transparency: int = 50
        self.word_wrap: bool = False
        self.word_wrap_width: int = 200

class TVCallout(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVCalloutOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Callout
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
