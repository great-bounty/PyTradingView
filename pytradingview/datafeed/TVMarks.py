"""
TradingView Marks and Timescale Marks
Structures for displaying marks on bars and timescale.
"""

from typing import Union, Dict, List, Optional
from .TVTypes import MarkColor, TimeScaleMarkShape


class TVMark:
    """
    Mark displayed on a bar in the chart.
    
    Marks are visual indicators on specific bars that can display
    text, labels, and optional images.
    
    Attributes:
        id: Unique identifier for the mark
        time: Mark time as Unix timestamp in seconds
        color: Mark color (constant name or custom color object)
        text: Text content for the mark
        label: Label for the mark
        labelFontColor: Text color for the mark label
        minSize: Minimum size for the mark
        borderWidth: Optional border width
        hoveredBorderWidth: Optional border width when hovering
        imageUrl: Optional URL for mark image
        showLabelWhenImageLoaded: Continue showing label when image loads (default: False)
    """
    def __init__(
        self,
        id: Union[str, int],
        time: int,
        color: Union[MarkColor, Dict[str, str]],
        text: str,
        label: str,
        labelFontColor: str,
        minSize: int,
        **kwargs
    ):
        self.id = id
        self.time = time
        self.color = color
        self.text = text
        self.label = label
        self.labelFontColor = labelFontColor
        self.minSize = minSize
        self.borderWidth = kwargs.get('borderWidth')
        self.hoveredBorderWidth = kwargs.get('hoveredBorderWidth')
        self.imageUrl = kwargs.get('imageUrl')
        self.showLabelWhenImageLoaded = kwargs.get('showLabelWhenImageLoaded', False)


class TVTimescaleMark:
    """
    Mark displayed on the timescale.
    
    Timescale marks appear on the time axis and can include
    labels, tooltips, and optional images.
    
    Attributes:
        id: Unique identifier for the timescale mark
        time: Mark time as Unix timestamp in seconds
        color: Mark color
        label: Label text for the mark
        tooltip: List of tooltip text lines
        labelFontColor: Optional text color (defaults to 'color' if not specified)
        shape: Optional mark shape
        imageUrl: Optional URL for mark image
        showLabelWhenImageLoaded: Continue showing label when image loads (default: False)
    """
    def __init__(
        self,
        id: Union[str, int],
        time: int,
        color: str,
        label: str,
        tooltip: List[str],
        **kwargs
    ):
        self.id = id
        self.time = time
        self.color = color
        self.label = label
        self.tooltip = tooltip
        self.labelFontColor = kwargs.get('labelFontColor')
        self.shape = kwargs.get('shape')
        self.imageUrl = kwargs.get('imageUrl')
        self.showLabelWhenImageLoaded = kwargs.get('showLabelWhenImageLoaded', False)


__all__ = [
    "TVMark",
    "TVTimescaleMark",
]
