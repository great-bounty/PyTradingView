
from typing import Any, Awaitable, Callable, Optional, Union
from ..core.TVObject import CallBackParams

class TVContextMenuItem(object):

    def __init__(self, text: str, position: str = "bottom", click: CallBackParams = None):
        self.text = text
        self.position = position
        self.click: CallBackParams = click