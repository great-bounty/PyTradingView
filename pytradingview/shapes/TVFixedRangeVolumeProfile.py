from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVFixedRangeVolumeProfileOverrides(TVBaseOverrides):

    def __init__(self):
        # Default value: `0`
        self.leftEnd = 0
        
        # Default value: `#2962FF`
        self.lineColor = "#2962FF"
        
        # Default value: `0`
        self.lineStyle = 0
        
        # Default value: `2`
        self.lineWidth = 2
        
        # Default value: `1`
        self.rightEnd = 1

class TVFixedRangeVolumeProfile(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVFixedRangeVolumeProfileOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.FixedRangeVolumeProfile
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
