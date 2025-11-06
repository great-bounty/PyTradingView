from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVFibRetracementOverrides(TVBaseOverrides):

    def __init__(self):
        self.coeffs_as_percents = False
        self.extend_lines = False
        self.extend_lines_left = False
        self.fib_levels_based_on_log_scale = False
        self.fill_background = True
        self.horz_labels_align = "left"
        self.horz_text_align = "center"
        self.label_font_size = 12

        self.level1_coeff = 0
        self.level1_color = "#787B86"
        self.level1_text = None
        self.level1_visible = True

        self.level10_coeff = 3.618
        self.level10_color = "#9c27b0"
        self.level10_text = None
        self.level10_visible = True

        self.level11_coeff = 4.236
        self.level11_color = "#e91e63"
        self.level11_text = None
        self.level11_visible = True

        self.level12_coeff = 1.272
        self.level12_color = "#FF9800"
        self.level12_text = None
        self.level12_visible = False

        self.level13_coeff = 1.414
        self.level13_color = "#F23645"
        self.level13_text = None
        self.level13_visible = False

        self.level14_coeff = 2.272
        self.level14_color = "#FF9800"
        self.level14_text = None
        self.level14_visible = False

        self.level15_coeff = 2.414
        self.level15_color = "#4caf50"
        self.level15_text = None
        self.level15_visible = False

        self.level16_coeff = 2
        self.level16_color = "#089981"
        self.level16_text = None
        self.level16_visible = False

        self.level17_coeff = 3
        self.level17_color = "#00bcd4"
        self.level17_text = None
        self.level17_visible = False

        self.level18_coeff = 3.272
        self.level18_color = "#787B86"
        self.level18_text = None
        self.level18_visible = False

        self.level19_coeff = 3.414
        self.level19_color = "#2962FF"
        self.level19_text = None
        self.level19_visible = False

        self.level2_coeff = 0.236
        self.level2_color = "#F23645"
        self.level2_text = None
        self.level2_visible = True

        self.level20_coeff = 4
        self.level20_color = "#F23645"
        self.level20_text = None
        self.level20_visible = False

        self.level21_coeff = 4.272
        self.level21_color = "#9c27b0"
        self.level21_text = None
        self.level21_visible = False

        self.level22_coeff = 4.414
        self.level22_color = "#e91e63"
        self.level22_text = None
        self.level22_visible = False

        self.level23_coeff = 4.618
        self.level23_color = "#FF9800"
        self.level23_text = None
        self.level23_visible = False

        self.level24_coeff = 4.764
        self.level24_color = "#089981"
        self.level24_text = None
        self.level24_visible = False

        self.level3_coeff = 0.382
        self.level3_color = "#FF9800"
        self.level3_text = None
        self.level3_visible = True

        self.level4_coeff = 0.5
        self.level4_color = "#4caf50"
        self.level4_text = None
        self.level4_visible = True

        self.level5_coeff = 0.618
        self.level5_color = "#089981"
        self.level5_text = None
        self.level5_visible = True

        self.level6_coeff = 0.786
        self.level6_color = "#00bcd4"
        self.level6_text = None
        self.level6_visible = True

        self.level7_coeff = 1
        self.level7_color = "#787B86"
        self.level7_text = None
        self.level7_visible = True

        self.level8_coeff = 1.618
        self.level8_color = "#2962FF"
        self.level8_text = None
        self.level8_visible = True

        self.level9_coeff = 2.618
        self.level9_color = "#F23645"
        self.level9_text = None
        self.level9_visible = True

        self.levels_style_linestyle = 0
        self.levels_style_linewidth = 2

        self.reverse = False
        self.show_coeffs = True
        self.show_prices = True
        self.show_text = True
        self.transparency = 80

        self.trendline_color = "#787B86"
        self.trendline_linestyle = 2
        self.trendline_linewidth = 2
        self.trendline_visible = True

        self.vert_labels_align = "middle"
        self.vert_text_align = "middle"

class TVFibRetracement(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVFibRetracementOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.FibRetracement
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
