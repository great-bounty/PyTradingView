from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVIconOverrides(TVBaseOverrides):

    def __init__(self):
        self.angle = 1.57
        self.color = "#2962FF"
        self.size = 40

class TVIcon(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVIconOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Icon
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
