from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVEmojiOverrides(TVBaseOverrides):

    def __init__(self):
        self.angle = 1.57
        self.size = 40

class TVEmoji(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVEmojiOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Emoji
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
