from tkinter import NO
from .TVBaseShape import TVSingleShapeType, TVBaseOverrides
from .TVSingleShape import TVSingleShape
from typing import Optional, Dict, Any

class TVArrowUpOverrides(TVBaseOverrides):

    def __init__(self):
        self.arrowColor = "#089981"
        self.bold = False
        self.color = "#089981"
        self.fontsize = 14
        self.italic = False
        self.showLabel = True

class TVArrowUp(TVSingleShape):
    
    def __init__(self, overrides: Optional[TVArrowUpOverrides] = None, **kwargs):
        self.shape = TVSingleShapeType.ArrowUp
        if overrides is None:
            super().__init__(shape=self.shape, **kwargs)
        else:
            super().__init__(shape=self.shape, overrides=overrides.to_json(), **kwargs)

        
