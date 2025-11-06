from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVExtendedOverrides(TVBaseOverrides):
    
    def __init__(self):
        self.alwaysShowStats = False
        self.bold = False
        self.extendLeft = True
        self.extendRight = True
        self.fontsize = 14
        self.horzLabelsAlign = "center"
        self.italic = False
        self.leftEnd = 0
        self.linecolor = "#2962FF"
        self.linestyle = 0
        self.linewidth = 2
        self.rightEnd = 0
        self.showAngle = False
        self.showBarsRange = False
        self.showDateTimeRange = False
        self.showDistance = False
        self.showLabel = False
        self.showMiddlePoint = False
        self.showPercentPriceRange = False
        self.showPipsPriceRange = False
        self.showPriceLabels = False
        self.showPriceRange = False
        self.statsPosition = 2
        self.textcolor = "#2962FF"
        self.vertLabelsAlign = "bottom"

class TVExtended(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVExtendedOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.Extended
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
