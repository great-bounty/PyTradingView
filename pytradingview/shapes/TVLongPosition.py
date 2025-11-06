from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVLongPositionOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.accountSize = 1000
        self.alwaysShowStats = False
        self.borderColor = "#667b8b"
        self.compact = False
        self.drawBorder = False
        self.fillBackground = True
        self.fillLabelBackground = True
        self.fontsize = 12
        self.labelBackgroundColor = "#585858"
        self.linecolor = "#787B86"
        self.linewidth = 1
        self.lotSize = 1
        self.profitBackground = "rgba(8, 153, 129, 0.2)"
        self.profitBackgroundTransparency = 80
        self.risk = 25
        self.riskDisplayMode = "percents"
        self.showPriceLabels = True
        self.stopBackground = "rgba(242, 54, 69, 0.2)"
        self.stopBackgroundTransparency = 80
        self.textcolor = "#ffffff"

class TVLongPosition(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVLongPositionOverrides] = None, **kwargs):
        shape = TVSingleShapeType.LongPosition
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
