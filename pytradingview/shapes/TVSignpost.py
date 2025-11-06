from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVSignpostOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.bold: bool = False
        self.emoji: str = "🙂"
        self.font_size: int = 12
        self.italic: bool = False
        self.plate_color: str = "#2962FF"
        self.show_image: bool = False

class TVSignpost(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVSignpostOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Signpost
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
