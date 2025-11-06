from .TVBaseShape import TVMultipleShapeType, TVBaseOverrides
from .TVMultipleShape import TVMultipleShape
from typing import Optional, Dict, Any

class TVTextNoteOverrides(TVBaseOverrides):

    def __init__(self):
        self.background_color = "rgba(91, 133, 191, 0.3)"
        self.background_transparency = 70
        self.bold = False
        self.border_color = "#667b8b"
        self.color = "#2962FF"
        self.draw_border = False
        self.fill_background = False
        self.fixed_size = True
        self.font_size = 14
        self.italic = False
        self.word_wrap = False
        self.word_wrap_width = 200

class TVTextNote(TVMultipleShape):
    
    def __init__(self, overrides: Optional[TVTextNoteOverrides] = None, **kwargs):
        shape = TVMultipleShapeType.TextNote
        if overrides is None:
            super().__init__(shape=shape, **kwargs)
        else:
            super().__init__(shape=shape, overrides=overrides.to_json(), **kwargs)

        
