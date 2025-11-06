
from typing import Optional
from .TVBaseShape import TVMultipleShapeType, TVBaseShape

class TVMultipleShape(TVBaseShape):
    def __init__(
        self, 
        shape: TVMultipleShapeType,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.shape: TVMultipleShapeType = shape