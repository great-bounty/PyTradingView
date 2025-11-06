from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVHighlighterOverrides(TVBaseOverrides):

    def __init__(self):
        self.line_color = "rgba(242, 54, 69, 0.2)"
        self.smooth = 5
        self.transparency = 80
        self.width = 20

class TVHighlighter(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVHighlighterOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Highlighter
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
