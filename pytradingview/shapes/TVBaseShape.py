from enum import Enum
from typing import Any, Union, Optional

class TVAnchorShapeType(Enum):
    AnchoredText = 'anchored_text'
    AnchoredNote = 'anchored_note'

class TVSingleShapeType(Enum):
    ArrowUp = 'arrow_up'
    ArrowDown = 'arrow_down'
    ArrowLeft = 'arrow_left'
    ArrowRight = 'arrow_right'
    Flag = 'flag'
    VerticalLine = 'vertical_line'
    HorizontalLine = 'horizontal_line'
    LongPosition = 'long_position'
    ShortPosition = 'short_position'
    Icon = 'icon'
    Emoji = 'emoji'
    Sticker = 'sticker'
    PriceLabel = 'price_label'
    PriceNote = 'price_note'
    ArrowMarker = 'arrow_marker'
    Balloon = 'balloon'
    Comment = 'comment'
    Callout = 'callout'
    Text = 'text'
    Note = 'note'
    Signpost = 'signpost'
    Table = 'table'

class TVMultipleShapeType(Enum):
    Triangle = 'triangle'
    Curve = 'curve'
    Circle = 'circle'
    Ellipse = 'ellipse'
    Path = 'path'
    Polyline = 'polyline'
    Extended = 'extended'
    DoubleCurve = 'double_curve'
    Arc = 'arc'
    CrossLine = 'cross_line'
    HorizontalRay = 'horizontal_ray'
    TrendLine = 'trend_line'
    InfoLine = 'info_line'
    TrendAngle = 'trend_angle'
    Arrow = 'arrow'
    Ray = 'ray'
    ParallelChannel = 'parallel_channel'
    DisjointAngle = 'disjoint_angle'
    FlatBottom = 'flat_bottom'
    AnchoredVwap = 'anchored_vwap'
    Pitchfork = 'pitchfork'
    SchiffPitchforkModified = 'schiff_pitchfork_modified'
    SchiffPitchfork = 'schiff_pitchfork'
    InsidePitchfork = 'inside_pitchfork'
    Pitchfan = 'pitchfan'
    Gannbox = 'gannbox'
    GannboxSquare = 'gannbox_square'
    GannboxFixed = 'gannbox_fixed'
    GannboxFan = 'gannbox_fan'
    FibRetracement = 'fib_retracement'
    FibTrendExt = 'fib_trend_ext'
    FibSpeedResistFan = 'fib_speed_resist_fan'
    FibTimezone = 'fib_timezone'
    FibTrendTime = 'fib_trend_time'
    FibCircles = 'fib_circles'
    FibSpiral = 'fib_spiral'
    FibSpeedResistArcs = 'fib_speed_resist_arcs'
    FibChannel = 'fib_channel'
    XabcdPattern = 'xabcd_pattern'
    CypherPattern = 'cypher_pattern'
    AbcdPattern = 'abcd_pattern'
    TextNote = 'text_note'
    TrianglePattern = 'triangle_pattern'
    ThreeDiversPattern = '3divers_pattern'
    HeadAndShoulders = 'head_and_shoulders'
    FibWedge = 'fib_wedge'
    ElliottImpulseWave = 'elliott_impulse_wave'
    ElliottTriangleWave = 'elliott_triangle_wave'
    ElliottTripleCombo = 'elliott_triple_combo'
    ElliottCorrection = 'elliott_correction'
    ElliottDoubleCombo = 'elliott_double_combo'
    CyclicLines = 'cyclic_lines'
    TimeCycles = 'time_cycles'
    SineLine = 'sine_line'
    Forecast = 'forecast'
    DateRange = 'date_range'
    PriceRange = 'price_range'
    DateAndPriceRange = 'date_and_price_range'
    BarsPattern = 'bars_pattern'
    GhostFeed = 'ghost_feed'
    Projection = 'projection'
    Rectangle = 'rectangle'
    RotatedRectangle = 'rotated_rectangle'
    Brush = 'brush'
    Highlighter = 'highlighter'
    RegressionTrend = 'regression_trend'
    FixedRangeVolumeProfile = 'fixed_range_volume_profile'

class TVBaseOverrides:
    
    def to_json(self) -> dict:
        result: dict[Any, Any] = {}
        
        for attr_name, attr_value in self.__dict__.items():
            if attr_value is None:
                continue
            
            if attr_name.startswith('_'):
                continue
            
            if callable(attr_value):
                continue
            
            if isinstance(attr_value, Enum):
                result[attr_name] = attr_value.value
            elif hasattr(attr_value, 'to_json'):
                result[attr_name] = attr_value.to_json()
            elif hasattr(attr_value, '__dict__'):
                result[attr_name] = {k: v for k, v in attr_value.__dict__.items() if not k.startswith('_')}
            elif isinstance(attr_value, (list, tuple)):
                result[attr_name] = [
                    item.to_json() if hasattr(item, 'to_json') 
                    else item
                    for item in attr_value
                ]
            else:
                result[attr_name] = attr_value
        
        return result

class TVBaseShape:
    def __init__(
        self,
        text: Optional[str] = None,
        lock: Optional[bool] = None,
        disable_selection: Optional[bool] = None,
        disable_save: Optional[bool] = None,
        disable_undo: Optional[bool] = None,
        overrides: Optional[dict] = None,
        z_order: Optional[str] = None, # ["top", "bottom"]
        show_in_objects_tree: Optional[bool] | None = None,
        owner_study_id: Optional[str] = None,
        filled: Optional[bool] = None,
        icon: Optional[int] = None
    ) -> None:
        self.text: Optional[str] = text
        self.lock: Optional[bool] = lock
        self.disable_selection: Optional[bool] = disable_selection
        self.disable_save: Optional[bool] = disable_save
        self.disable_undo: Optional[bool] = disable_undo
        self.overrides: Optional[dict] = overrides
        self.z_order: Optional[str] = z_order
        self.show_in_objects_tree: Optional[bool] = show_in_objects_tree
        self.owner_study_id: Optional[str] = owner_study_id
        self.filled: Optional[bool] = filled
        self.icon: Optional[int] = icon

    def to_json(self) -> dict:
        result: dict[Any, Any] = {}
        
        for attr_name, attr_value in self.__dict__.items():
            if attr_value is None:
                continue
            
            if attr_name.startswith('_'):
                continue
            
            if callable(attr_value):
                continue
            
            if isinstance(attr_value, Enum):
                result[attr_name] = attr_value.value
            elif hasattr(attr_value, 'to_json'):
                result[attr_name] = attr_value.to_json()
            elif hasattr(attr_value, '__dict__'):
                result[attr_name] = {k: v for k, v in attr_value.__dict__.items() if not k.startswith('_')}
            elif isinstance(attr_value, (list, tuple)):
                result[attr_name] = [
                    item.to_json() if hasattr(item, 'to_json') 
                    else item
                    for item in attr_value
                ]
            else:
                result[attr_name] = attr_value
        
        return result