from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVTextOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.backgroundColor: str = "rgba(91, 133, 191, 0.3)"
        self.backgroundTransparency: int = 70
        self.bold: bool = False
        self.borderColor: str = "#667b8b"
        self.color: str = "#2962FF"
        self.drawBorder: bool = False
        self.fillBackground: bool = False
        self.fixedSize: bool = True
        self.fontsize: int = 14
        self.italic: bool = False
        self.wordWrap: bool = False
        self.wordWrapWidth: int = 200

class TVText(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVTextOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Text
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
