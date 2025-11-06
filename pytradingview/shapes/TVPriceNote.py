from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVPriceNoteOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.backgroundColor: str = "#2962FF"
        self.borderColor: str = "#2962FF"
        self.color: str = "#ffffff"
        self.fontsize: int = 14
        self.fontWeight: str = "bold"
        self.transparency: int = 0

class TVPriceNote(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVPriceNoteOverrides] = None, **kwargs):
        shape = TVSingleShapeType.PriceNote
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
