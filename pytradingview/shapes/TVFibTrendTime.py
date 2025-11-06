from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVFibTrendTimeOverrides(TVBaseOverrides):

    def __init__(self):
        self.fill_background = False
        self.horz_labels_align = "right"

        self.level1_coeff = 0
        self.level1_color = "#787B86"
        self.level1_linestyle = 0
        self.level1_linewidth = 2
        self.level1_visible = True

        self.level2_coeff = 1
        self.level2_color = "#2962FF"
        self.level2_linestyle = 0
        self.level2_linewidth = 2
        self.level2_visible = True

        self.level3_coeff = 2
        self.level3_color = "#2962FF"
        self.level3_linestyle = 0
        self.level3_linewidth = 2
        self.level3_visible = True

        self.level4_coeff = 3
        self.level4_color = "#2962FF"
        self.level4_linestyle = 0
        self.level4_linewidth = 2
        self.level4_visible = True

        self.level5_coeff = 5
        self.level5_color = "#2962FF"
        self.level5_linestyle = 0
        self.level5_linewidth = 2
        self.level5_visible = True

        self.level6_coeff = 8
        self.level6_color = "#2962FF"
        self.level6_linestyle = 0
        self.level6_linewidth = 2
        self.level6_visible = True

        self.level7_coeff = 13
        self.level7_color = "#2962FF"
        self.level7_linestyle = 0
        self.level7_linewidth = 2
        self.level7_visible = True

        self.level8_coeff = 21
        self.level8_color = "#2962FF"
        self.level8_linestyle = 0
        self.level8_linewidth = 2
        self.level8_visible = True

        self.level9_coeff = 34
        self.level9_color = "#2962FF"
        self.level9_linestyle = 0
        self.level9_linewidth = 2
        self.level9_visible = True

        self.level10_coeff = 55
        self.level10_color = "#2962FF"
        self.level10_linestyle = 0
        self.level10_linewidth = 2
        self.level10_visible = True

        self.level11_coeff = 89
        self.level11_color = "#2962FF"
        self.level11_linestyle = 0
        self.level11_linewidth = 2
        self.level11_visible = True

        self.show_labels = True
        self.transparency = 80

        self.trendline_color = "#808080"
        self.trendline_linestyle = 2
        self.trendline_linewidth = 1
        self.trendline_visible = True

        self.vert_labels_align = "bottom"

class TVFibTrendTime(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVFibTrendTimeOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.FibTrendTime
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
