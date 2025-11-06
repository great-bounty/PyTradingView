from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVFlagMarkOverrides(TVBaseOverrides):

    def __init__(self):
        self.flagColor: str = "#2962FF"

class TVFlagMark(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVFlagMarkOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Flag
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
