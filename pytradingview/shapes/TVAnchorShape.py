
from typing import Optional
from .TVBaseShape import TVAnchorShapeType, TVBaseShape

class TVAnchorShape(TVBaseShape):
    def __init__(
        self, 
        shape: TVAnchorShapeType, 
        owner_study_id: Optional[str] = None,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.shape: TVAnchorShapeType = shape
        self.owner_study_id: Optional[str] = owner_study_id