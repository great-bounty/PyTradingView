from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVInsidePitchforkOverrides(TVBaseOverrides):
    
    def __init__(self):
        self.extend_lines = False
        self.fill_background = True

        self.level0_coeff = 0.25
        self.level0_color = "#ffb74d"
        self.level0_linestyle = 0
        self.level0_linewidth = 2
        self.level0_visible = False

        self.level1_coeff = 0.382
        self.level1_color = "#81c784"
        self.level1_linestyle = 0
        self.level1_linewidth = 2
        self.level1_visible = False

        self.level2_coeff = 0.5
        self.level2_color = "#089981"
        self.level2_linestyle = 0
        self.level2_linewidth = 2
        self.level2_visible = True

        self.level3_coeff = 0.618
        self.level3_color = "#089981"
        self.level3_linestyle = 0
        self.level3_linewidth = 2
        self.level3_visible = False

        self.level4_coeff = 0.75
        self.level4_color = "#00bcd4"
        self.level4_linestyle = 0
        self.level4_linewidth = 2
        self.level4_visible = False

        self.level5_coeff = 1
        self.level5_color = "#2962FF"
        self.level5_linestyle = 0
        self.level5_linewidth = 2
        self.level5_visible = True

        self.level6_coeff = 1.5
        self.level6_color = "#9c27b0"
        self.level6_linestyle = 0
        self.level6_linewidth = 2
        self.level6_visible = False

        self.level7_coeff = 1.75
        self.level7_color = "#e91e63"
        self.level7_linestyle = 0
        self.level7_linewidth = 2
        self.level7_visible = False

        self.level8_coeff = 2
        self.level8_color = "#F77C80"
        self.level8_linestyle = 0
        self.level8_linewidth = 2
        self.level8_visible = False

        self.median_color = "#F23645"
        self.median_linestyle = 0
        self.median_linewidth = 2
        self.median_visible = True

        self.style = 2
        self.transparency = 80

class TVInsidePitchfork(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVInsidePitchforkOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.InsidePitchfork
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)