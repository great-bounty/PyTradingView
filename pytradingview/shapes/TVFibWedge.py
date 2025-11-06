from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVFibWedgeOverrides(TVBaseOverrides):

    def __init__(self):
        self.fill_background = True

        self.level1_coeff = 0.236
        self.level1_color = "#F23645"
        self.level1_linestyle = 0
        self.level1_linewidth = 2
        self.level1_visible = True

        self.level2_coeff = 0.382
        self.level2_color = "#FF9800"
        self.level2_linestyle = 0
        self.level2_linewidth = 2
        self.level2_visible = True

        self.level3_coeff = 0.5
        self.level3_color = "#4caf50"
        self.level3_linestyle = 0
        self.level3_linewidth = 2
        self.level3_visible = True

        self.level4_coeff = 0.618
        self.level4_color = "#089981"
        self.level4_linestyle = 0
        self.level4_linewidth = 2
        self.level4_visible = True

        self.level5_coeff = 0.786
        self.level5_color = "#00bcd4"
        self.level5_linestyle = 0
        self.level5_linewidth = 2
        self.level5_visible = True

        self.level6_coeff = 1
        self.level6_color = "#787B86"
        self.level6_linestyle = 0
        self.level6_linewidth = 2
        self.level6_visible = True

        self.level7_coeff = 1.618
        self.level7_color = "#2962FF"
        self.level7_linestyle = 0
        self.level7_linewidth = 2
        self.level7_visible = False

        self.level8_coeff = 2.618
        self.level8_color = "#F23645"
        self.level8_linestyle = 0
        self.level8_linewidth = 2
        self.level8_visible = False

        self.level9_coeff = 3.618
        self.level9_color = "#673ab7"
        self.level9_linestyle = 0
        self.level9_linewidth = 2
        self.level9_visible = False

        self.level10_coeff = 4.236
        self.level10_color = "#e91e63"
        self.level10_linestyle = 0
        self.level10_linewidth = 2
        self.level10_visible = False

        self.level11_coeff = 4.618
        self.level11_color = "#e91e63"
        self.level11_linestyle = 0
        self.level11_linewidth = 2
        self.level11_visible = False

        self.show_coeffs = True
        self.transparency = 80

        self.trendline_color = "#808080"
        self.trendline_linestyle = 0
        self.trendline_linewidth = 2
        self.trendline_visible = True

class TVFibWedge(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVFibWedgeOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.FibWedge
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
