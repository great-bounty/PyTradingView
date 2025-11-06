from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVRegressionTrendOverrides(TVBaseOverrides):

    def __init__(self):
        self.inputs_first_bar_time = 0
        self.inputs_last_bar_time = 0
        self.inputs_lower_diviation = -2
        self.inputs_source = "close"
        self.inputs_upper_diviation = 2
        self.inputs_use_lower_diviation = True
        self.inputs_use_upper_diviation = True
        self.linestyle = 0
        self.linewidth = 1
        self.precision = "default"
        self.styles_base_line_color = "rgba(242, 54, 69, 0.3)"
        self.styles_base_line_display = 15
        self.styles_base_line_linestyle = 2
        self.styles_base_line_linewidth = 1
        self.styles_down_line_color = "rgba(41, 98, 255, 0.3)"
        self.styles_down_line_display = 15
        self.styles_down_line_linestyle = 0
        self.styles_down_line_linewidth = 2
        self.styles_extend_lines = False
        self.styles_show_pearsons = True
        self.styles_transparency = 70
        self.styles_up_line_color = "rgba(41, 98, 255, 0.3)"
        self.styles_up_line_display = 15
        self.styles_up_line_linestyle = 0
        self.styles_up_line_linewidth = 2

class TVRegressionTrend(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVRegressionTrendOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.RegressionTrend
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
