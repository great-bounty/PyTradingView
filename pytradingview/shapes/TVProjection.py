from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVProjectionOverrides(TVBaseOverrides):

    def __init__(self):
        self.color1 = "rgba(41, 98, 255, 0.2)"
        self.color2 = "rgba(156, 39, 176, 0.2)"
        self.fill_background = True
        self.level1_coeff = 1
        self.level1_color = "#808080"
        self.level1_linestyle = 0
        self.level1_linewidth = 2
        self.level1_visible = True
        self.linewidth = 2
        self.show_coeffs = True
        self.transparency = 80
        self.trendline_color = "#9598A1"
        self.trendline_linestyle = 0
        self.trendline_visible = True

class TVProjection(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVProjectionOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Projection
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
