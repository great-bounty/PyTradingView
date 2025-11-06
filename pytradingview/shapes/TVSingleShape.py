
from typing import Optional
from .TVBaseShape import TVSingleShapeType, TVBaseShape

class TVSingleShape(TVBaseShape):
    def __init__(
        self, 
        shape: TVSingleShapeType, 
        owner_study_id: Optional[str] = None,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.shape: TVSingleShapeType = shape
        self.owner_study_id: Optional[str] = owner_study_id