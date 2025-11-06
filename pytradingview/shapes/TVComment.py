from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVCommentOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.backgroundColor: str = "#2962FF"
        self.borderColor: str = "#2962FF"
        self.color: str = "#ffffff"
        self.fontsize: int = 16
        self.transparency: int = 0

class TVComment(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVCommentOverrides] = None, **kwargs):
        shape = TVSingleShapeType.Comment
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
