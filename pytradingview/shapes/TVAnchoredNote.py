from .TVBaseShape import TVAnchorShapeType, TVBaseOverrides
from .TVAnchorShape import TVAnchorShape
from typing import Optional, Dict, Any

class TVAnchoredNoteOverrides(TVBaseOverrides):

    def __init__(self) -> None:
        self.backgroundColor = "rgba(155, 190, 213, 0.3)"
        self.backgroundTransparency = 70
        self.bold = False
        self.borderColor = "#667b8b"
        self.color = "#2962FF"
        self.drawBorder = False
        self.fillBackground = False
        self.fixedSize = False
        self.fontsize = 14
        self.italic = False
        self.wordWrap = False
        self.wordWrapWidth = 200

class TVAnchoredNote(TVAnchorShape):
    
    def __init__(self, overrides: Optional[TVAnchoredNoteOverrides] = None, **kwargs):
        shape = TVAnchorShapeType.AnchoredNote
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)