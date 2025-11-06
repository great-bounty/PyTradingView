from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVAnchoredVwapOverrides(TVBaseOverrides):
    def __init__(self):
        self.background_1_color = "#4caf50"
        self.background_1_transparency = 95
        self.background_1_visible = True

        self.vwap_display = 15
        self.vwap_color = "#1e88e5"
        self.vwap_linestyle = 0
        self.vwap_linewidth = 1
        self.vwap_plottype = "line"
        self.vwap_trackprice = False
        self.vwap_transparency = 0

        self.lower_band_1_display = 15
        self.lower_band_1_color = "#4caf50"
        self.lower_band_1_linestyle = 0
        self.lower_band_1_linewidth = 1
        self.lower_band_1_plottype = "line"
        self.lower_band_1_trackprice = False
        self.lower_band_1_transparency = 0

        self.lower_band_2_display = 15
        self.lower_band_2_color = "#808000"
        self.lower_band_2_linestyle = 0
        self.lower_band_2_linewidth = 1
        self.lower_band_2_plottype = "line"
        self.lower_band_2_trackprice = False
        self.lower_band_2_transparency = 0

        self.lower_band_3_display = 15
        self.lower_band_3_color = "#00897b"
        self.lower_band_3_linestyle = 0
        self.lower_band_3_linewidth = 1
        self.lower_band_3_plottype = "line"
        self.lower_band_3_trackprice = False
        self.lower_band_3_transparency = 0

        self.upper_band_1_display = 15
        self.upper_band_1_color = "#4caf50"
        self.upper_band_1_linestyle = 0
        self.upper_band_1_linewidth = 1
        self.upper_band_1_plottype = "line"
        self.upper_band_1_trackprice = False
        self.upper_band_1_transparency = 0

        self.upper_band_2_display = 15
        self.upper_band_2_color = "#808000"
        self.upper_band_2_linestyle = 0
        self.upper_band_2_linewidth = 1
        self.upper_band_2_plottype = "line"
        self.upper_band_2_trackprice = False
        self.upper_band_2_transparency = 0

        self.upper_band_3_display = 15
        self.upper_band_3_color = "#00897b"
        self.upper_band_3_linestyle = 0
        self.upper_band_3_linewidth = 1
        self.upper_band_3_plottype = "line"
        self.upper_band_3_trackprice = False
        self.upper_band_3_transparency = 0

class TVAnchoredVwap(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVAnchoredVwapOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.AnchoredVwap
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)