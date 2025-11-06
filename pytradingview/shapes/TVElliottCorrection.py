from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVElliottCorrectionOverrides(TVBaseOverrides):

    def __init__(self):
        self.color = "#3d85c6"
        self.degree = 7
        self.line_width = 2
        self.show_wave = True

class TVElliottCorrection(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVElliottCorrectionOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.ElliottCorrection
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
