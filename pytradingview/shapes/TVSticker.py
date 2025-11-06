from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVStickerOverrides(TVBaseOverrides):

    def __init__(self):
        self.angle = 1.57
        self.size = 110

class TVSticker(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVStickerOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Sticker
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
