from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVHeadAndShouldersOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "#089981"
        self.bold = False
        self.color = "#089981"
        self.fill_background = True
        self.font_size = 12
        self.italic = False
        self.line_width = 2
        self.text_color = "#ffffff"
        self.transparency = 85

class TVHeadAndShoulders(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVHeadAndShouldersOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.HeadAndShoulders
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
