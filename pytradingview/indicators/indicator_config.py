"""
Indicator Configuration System - Complete Configuration Management Framework

Provides a powerful and flexible indicator configuration system that supports:
1. Complex input parameter types (numbers, strings, colors, booleans, options, etc.)
2. Style configuration
3. Runtime dynamic modification
4. Automatic UI generation
5. Validation and serialization
"""

from typing import Any, Optional, Dict, List, Tuple, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
import json


class InputType(Enum):
    """Input parameter type enumeration"""
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    STRING = "string"
    COLOR = "color"
    OPTIONS = "options"  # Dropdown options
    SOURCE = "source"    # Data source (open, high, low, close, hl2, hlc3, ohlc4)


@dataclass
class InputOption:
    """Single option for option type"""
    label: str  # Display label
    value: Any  # Actual value
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'label': self.label,
            'value': self.value
        }


@dataclass
class InputDefinition:
    """
    Input parameter definition
    
    Defines all characteristics of a single input parameter for an indicator
    """
    # Parameter identifier (field name)
    id: str
    
    # Display name (shown in UI)
    display_name: str
    
    # Parameter type
    type: InputType
    
    # Default value
    default_value: Any
    
    # Current value (modifiable at runtime)
    value: Any = None
    
    # Tooltip
    tooltip: str = ""
    
    # Options list (only used when type=OPTIONS)
    options: List[InputOption] = field(default_factory=list)
    
    # Minimum value (for numeric types)
    min_value: Optional[Union[int, float]] = None
    
    # Maximum value (for numeric types)
    max_value: Optional[Union[int, float]] = None
    
    # Step value (for numeric types)
    step: Optional[Union[int, float]] = None
    
    # Whether to display in UI
    visible: bool = True
    
    # Group (for UI categorization)
    group: str = "Parameters"
    
    def __post_init__(self):
        """Post-initialization processing"""
        if self.value is None:
            self.value = self.default_value
    
    def validate(self) -> Tuple[bool, Optional[str]]:
        """
        Validate whether the current value is valid
        
        Returns:
            (is_valid, error_message): Whether valid, error message
        """
        # Type validation
        if self.type == InputType.INTEGER:
            if not isinstance(self.value, int):
                return False, f"Value must be an integer, got {type(self.value).__name__}"
            if self.min_value is not None and self.value < self.min_value:
                return False, f"Value {self.value} is less than minimum {self.min_value}"
            if self.max_value is not None and self.value > self.max_value:
                return False, f"Value {self.value} is greater than maximum {self.max_value}"
        
        elif self.type == InputType.FLOAT:
            if not isinstance(self.value, (int, float)):
                return False, f"Value must be a number, got {type(self.value).__name__}"
            if self.min_value is not None and self.value < self.min_value:
                return False, f"Value {self.value} is less than minimum {self.min_value}"
            if self.max_value is not None and self.value > self.max_value:
                return False, f"Value {self.value} is greater than maximum {self.max_value}"
        
        elif self.type == InputType.BOOLEAN:
            if not isinstance(self.value, bool):
                return False, f"Value must be a boolean, got {type(self.value).__name__}"
        
        elif self.type == InputType.STRING:
            if not isinstance(self.value, str):
                return False, f"Value must be a string, got {type(self.value).__name__}"
        
        elif self.type == InputType.COLOR:
            if not isinstance(self.value, str):
                return False, f"Color must be a string, got {type(self.value).__name__}"
            # Simple color format validation (#RGB or #RRGGBB)
            if not self.value.startswith('#'):
                return False, f"Color must start with #, got {self.value}"
            if len(self.value) not in (4, 7):
                return False, f"Invalid color format: {self.value}"
        
        elif self.type == InputType.OPTIONS:
            # Check if value is in options
            valid_values = [opt.value for opt in self.options]
            if self.value not in valid_values:
                return False, f"Value {self.value} is not in valid options: {valid_values}"
        
        elif self.type == InputType.SOURCE:
            # Validate data source
            valid_sources = ['open', 'high', 'low', 'close', 'hl2', 'hlc3', 'ohlc4', 'volume']
            if self.value not in valid_sources:
                return False, f"Invalid source: {self.value}. Must be one of {valid_sources}"
        
        return True, None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary (for serialization)"""
        return {
            'id': self.id,
            'display_name': self.display_name,
            'type': self.type.value,
            'default_value': self.default_value,
            'value': self.value,
            'tooltip': self.tooltip,
            'options': [opt.to_dict() for opt in self.options],
            'min_value': self.min_value,
            'max_value': self.max_value,
            'step': self.step,
            'visible': self.visible,
            'group': self.group
        }


@dataclass
class StyleDefinition:
    """
    Style definition
    
    Defines style configuration for indicator plotting
    """
    # Style identifier
    id: str
    
    # Display name
    display_name: str
    
    # Color
    color: str
    
    # Line width (0-10)
    line_width: int = 1
    
    # Line style (0=solid, 1=dashed, 2=dotted)
    line_style: int = 0
    
    # Transparency (0-100)
    transparency: int = 0
    
    # Whether to display
    visible: bool = True
    
    # Group
    group: str = "Style"
    
    def validate(self) -> Tuple[bool, Optional[str]]:
        """Validate style configuration"""
        if not isinstance(self.color, str) or not self.color.startswith('#'):
            return False, f"Invalid color: {self.color}"
        
        if not (0 <= self.line_width <= 10):
            return False, f"Line width must be 0-10, got {self.line_width}"
        
        if self.line_style not in (0, 1, 2):
            return False, f"Line style must be 0, 1, or 2, got {self.line_style}"
        
        if not (0 <= self.transparency <= 100):
            return False, f"Transparency must be 0-100, got {self.transparency}"
        
        return True, None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'display_name': self.display_name,
            'color': self.color,
            'line_width': self.line_width,
            'line_style': self.line_style,
            'transparency': self.transparency,
            'visible': self.visible,
            'group': self.group
        }


@dataclass
class IndicatorConfig:
    """
    Indicator configuration base class
    
    This is a complete configuration system that supports:
    1. Complex input parameter definitions (numbers, strings, colors, booleans, options, etc.)
    2. Style configuration
    3. Runtime dynamic modification
    4. Automatic UI generation
    5. Validation and serialization
    """
    
    # === Basic Information ===
    name: str = "CustomIndicator"
    version: str = "1.0.0"
    description: str = ""
    author: str = ""
    
    # === Status ===
    enabled: bool = True
    debug: bool = False
    
    # === Input Parameter Definitions ===
    inputs: List[InputDefinition] = field(default_factory=list)
    
    # === Style Definitions ===
    styles: List[StyleDefinition] = field(default_factory=list)
    
    # === Change Callback ===
    # Called when configuration changes, passed the changed key-value pairs
    on_config_changed: Optional[Callable[[Dict[str, Any]], None]] = None
    
    def get_input_value(self, input_id: str) -> Any:
        """Get the current value of an input parameter"""
        for inp in self.inputs:
            if inp.id == input_id:
                return inp.value
        return None
    
    def set_input_value(self, input_id: str, value: Any) -> Tuple[bool, Optional[str]]:
        """
        Set the value of an input parameter
        
        Args:
            input_id: Parameter ID
            value: New value
            
        Returns:
            (success, error_message): Whether set successfully, error message
        """
        for inp in self.inputs:
            if inp.id == input_id:
                old_value = inp.value
                inp.value = value
                
                # Validate
                is_valid, error = inp.validate()
                if not is_valid:
                    inp.value = old_value  # Restore old value
                    return False, error
                
                # Trigger callback
                if self.on_config_changed:
                    try:
                        self.on_config_changed({input_id: value})
                    except Exception as e:
                        inp.value = old_value  # Callback failed, restore old value
                        return False, f"Config changed callback failed: {str(e)}"
                
                return True, None
        
        return False, f"Input '{input_id}' not found"
    
    def set_input_values(self, values: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Set multiple input parameters in batch
        
        Args:
            values: Mapping from parameter IDs to values
            
        Returns:
            (success, errors): Whether all succeeded, list of error messages
        """
        errors = []
        for input_id, value in values.items():
            success, error = self.set_input_value(input_id, value)
            if not success:
                errors.append(f"{input_id}: {error}")
        
        return len(errors) == 0, errors
    
    def get_style(self, style_id: str) -> Optional[StyleDefinition]:
        """Get style definition"""
        for style in self.styles:
            if style.id == style_id:
                return style
        return None
    
    def update_style(self, style_id: str, **kwargs) -> Tuple[bool, Optional[str]]:
        """
        Update style properties
        
        Args:
            style_id: Style ID
            **kwargs: Properties to update
            
        Returns:
            (success, error_message): Whether update succeeded, error message
        """
        style = self.get_style(style_id)
        if not style:
            return False, f"Style '{style_id}' not found"
        
        # Save old values
        old_values = {}
        for key in kwargs:
            if hasattr(style, key):
                old_values[key] = getattr(style, key)
        
        # Apply new values
        for key, value in kwargs.items():
            if hasattr(style, key):
                setattr(style, key, value)
        
        # Validate
        is_valid, error = style.validate()
        if not is_valid:
            # Restore old values
            for key, value in old_values.items():
                setattr(style, key, value)
            return False, error
        
        # Trigger callback
        if self.on_config_changed:
            try:
                self.on_config_changed({f"{style_id}.{k}": v for k, v in kwargs.items()})
            except Exception as e:
                # Restore old values
                for key, value in old_values.items():
                    setattr(style, key, value)
                return False, f"Config changed callback failed: {str(e)}"
        
        return True, None
    
    def validate_all(self) -> Tuple[bool, List[str]]:
        """
        Validate all input parameters and styles
        
        Returns:
            (is_valid, errors): Whether all valid, list of error messages
        """
        errors = []
        
        # Validate input parameters
        for inp in self.inputs:
            is_valid, error = inp.validate()
            if not is_valid:
                errors.append(f"Input '{inp.display_name}': {error}")
        
        # Validate styles
        for style in self.styles:
            is_valid, error = style.validate()
            if not is_valid:
                errors.append(f"Style '{style.display_name}': {error}")
        
        return len(errors) == 0, errors
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary (for serialization and UI)"""
        return {
            # Basic information
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'author': self.author,
            'enabled': self.enabled,
            'debug': self.debug,
            
            # Input parameters
            'inputs': [inp.to_dict() for inp in self.inputs],
            
            # Styles
            'styles': [style.to_dict() for style in self.styles]
        }
    
    def to_json(self, indent: int = 2) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
    
    def from_dict(self, data: Dict[str, Any]) -> 'IndicatorConfig':
        """
        Restore configuration from dictionary
        
        Args:
            data: Configuration dictionary
            
        Returns:
            self: Supports method chaining
        """
        # Update basic information
        if 'enabled' in data:
            self.enabled = data['enabled']
        if 'debug' in data:
            self.debug = data['debug']
        
        # Update input parameter values
        if 'inputs' in data:
            input_values = {}
            for inp_data in data['inputs']:
                inp_id = inp_data.get('id')
                inp_value = inp_data.get('value')
                if inp_id and inp_value is not None:
                    input_values[inp_id] = inp_value
            
            if input_values:
                success, errors = self.set_input_values(input_values)
                if not success:
                    raise ValueError(f"Failed to set input values: {errors}")
        
        # Update styles
        if 'styles' in data:
            for style_data in data['styles']:
                style_id = style_data.get('id')
                if style_id:
                    style_updates = {k: v for k, v in style_data.items() if k != 'id'}
                    if style_updates:
                        success, error = self.update_style(style_id, **style_updates)
                        if not success:
                            raise ValueError(f"Failed to update style '{style_id}': {error}")
        
        return self
    
    def from_json(self, json_str: str) -> 'IndicatorConfig':
        """Restore configuration from JSON string"""
        data = json.loads(json_str)
        return self.from_dict(data)
    
    def reset_to_defaults(self) -> None:
        """Reset all parameters to default values"""
        for inp in self.inputs:
            inp.value = inp.default_value
        
        # Trigger callback
        if self.on_config_changed:
            self.on_config_changed({'_reset': True})
    
    def get_inputs_by_group(self) -> Dict[str, List[InputDefinition]]:
        """Get input parameters grouped by category"""
        groups: Dict[str, List[InputDefinition]] = {}
        for inp in self.inputs:
            if inp.group not in groups:
                groups[inp.group] = []
            groups[inp.group].append(inp)
        return groups
    
    def get_styles_by_group(self) -> Dict[str, List[StyleDefinition]]:
        """Get styles grouped by category"""
        groups: Dict[str, List[StyleDefinition]] = {}
        for style in self.styles:
            if style.group not in groups:
                groups[style.group] = []
            groups[style.group].append(style)
        return groups
