from typing import Any, Union, Literal, Optional
import pandas as pd

class TVTimeFieldDescriptor:
    """
    Used in the schema defined in exportData API to describe the time field.
    This is used when `includeTime: true` is defined in `exportData` to add time to exported data.
    """
    
    def __init__(self):
        """Initialize a time field descriptor with type 'time'."""
        self.type: Literal["time"] = "time"

    def to_json(self) -> dict[str, Any]:
        """
        Convert the time field descriptor to JSON format.
        
        :return: Dictionary containing the field descriptor in JSON format
        """
        return {"type": self.type}


class TVUserTimeFieldDescriptor:
    """
    Used in the schema defined in exportData API to describe the user time field.
    This is used when `includeUserTime: true` is defined in `exportData` to add user time 
    (aka time that is displayed to the user on the chart) to exported data.
    """
    
    def __init__(self):
        """Initialize a user time field descriptor with type 'userTime'."""
        self.type: Literal["userTime"] = "userTime"

    def to_json(self) -> dict[str, Any]:
        """
        Convert the user time field descriptor to JSON format.
        
        :return: Dictionary containing the field descriptor in JSON format
        """
        return {"type": self.type}


class TVSeriesFieldDescriptor:
    """
    Description of a series field.
    This is used when `includeSeries: true` is defined in `exportData`.
    """
    
    def __init__(self):
        """Initialize a series field descriptor."""
        self.type: Literal["value"] = "value"  # Type is a 'value'
        self.sourceType: Literal["series"] = "series"  # Source type is a 'series'
        self.plotTitle = ""  # The name of the plot (open, high, low, close)
        self.sourceTitle = ""  # Title of the series

    def to_json(self) -> dict[str, Any]:
        """
        Convert the series field descriptor to JSON format.
        
        :return: Dictionary containing the field descriptor in JSON format
        """
        return {
            "type": self.type,
            "sourceType": self.sourceType,
            "plotTitle": self.plotTitle,
            "sourceTitle": self.sourceTitle,
        }


class TVStudyFieldDescriptor:
    """
    Description of a study field.
    This is used when `includedStudies: true` is defined in `exportData`.
    """
    
    def __init__(self):
        """Initialize a study field descriptor."""
        self.type: Literal["value"] = "value"  # Type is a 'value'
        self.sourceType: Literal["study"] = "study"  # Source type is a 'study'
        self.sourceId = ""  # The ID of the source study
        self.sourceTitle = ""  # The title of the source study
        self.plotTitle = ""  # The title of the source plot

    def to_json(self) -> dict[str, Any]:
        """
        Convert the study field descriptor to JSON format.
        
        :return: Dictionary containing the field descriptor in JSON format
        """
        return {
            "type": self.type,
            "sourceType": self.sourceType,
            "sourceId": self.sourceId,
            "sourceTitle": self.sourceTitle,
            "plotTitle": self.plotTitle,
        }


# Field descriptor union type
TVFieldDescriptor = Union[
    TVTimeFieldDescriptor,
    TVUserTimeFieldDescriptor,
    TVSeriesFieldDescriptor,
    TVStudyFieldDescriptor,
]


class TVExportedData:
    """
    Export data from the chart.
    Corresponds to the ExportedData interface in TypeScript.
    """
    
    def __init__(self):
        """Initialize an empty exported data object."""
        self.indexes: list[int] = []  # Array of data point indexes
        self.schema: list[TVFieldDescriptor] = []  # An array of field descriptors
        self.data: list[list[float]] = []  # Array of the same length as schema that represents the associated field's item
        self.displayedData: list[list[str]] = []  # Array of strings that represents the display value of the associated field element

    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> "TVExportedData":
        """
        Create a TVExportedData instance from JSON data.
        
        :param json_data: JSON data received from the frontend
        :return: TVExportedData instance
        """
        instance = cls()
        
        # Parse schema field
        schema_list = json_data.get("schema", [])
        for field in schema_list:
            field_type = field.get("type")
            if field_type == "time":
                descriptor = TVTimeFieldDescriptor()
                instance.schema.append(descriptor)
            elif field_type == "userTime":
                descriptor = TVUserTimeFieldDescriptor()
                instance.schema.append(descriptor)
            elif field_type == "value":
                source_type = field.get("sourceType")
                if source_type == "series":
                    descriptor = TVSeriesFieldDescriptor()
                    descriptor.plotTitle = field.get("plotTitle", "")
                    descriptor.sourceTitle = field.get("sourceTitle", "")
                    instance.schema.append(descriptor)
                elif source_type == "study":
                    descriptor = TVStudyFieldDescriptor()
                    descriptor.sourceId = field.get("sourceId", "")
                    descriptor.sourceTitle = field.get("sourceTitle", "")
                    descriptor.plotTitle = field.get("plotTitle", "")
                    instance.schema.append(descriptor)
        
        # Parse data field (Float64Array[] converted to list[list[float]])
        instance.data = json_data.get("data", [])
        
        # Parse displayedData field
        instance.displayedData = json_data.get("displayedData", [])

        instance.indexes = json_data.get("indexes", [])
        
        return instance

    def to_json(self) -> dict[str, Any]:
        """
        Convert the TVExportedData instance to JSON format.
        
        :return: Dictionary in JSON format
        """
        return {
            "schema": [field.to_json() for field in self.schema],
            "data": self.data,
            "displayedData": self.displayedData,
            "indexes": self.indexes
        }

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the TVExportedData instance to a pandas DataFrame.
        
        :return: pandas DataFrame instance
        """
        if not self.data or not self.schema:
            return pd.DataFrame()
        
        df_data = {}
        
        for idx, field in enumerate(self.schema):
            field_key = str(idx)
            
            if isinstance(field, TVTimeFieldDescriptor):
                column_name = 'time'
            elif isinstance(field, TVUserTimeFieldDescriptor):
                column_name = 'userTime'
            elif isinstance(field, TVSeriesFieldDescriptor):
                column_name = field.plotTitle.lower() if field.plotTitle else f'series_{idx}'
            elif isinstance(field, TVStudyFieldDescriptor):
                column_name = field.plotTitle if field.plotTitle else f'study_{idx}'
            else:
                column_name = f'column_{idx}'
            
            values = []
            for row in self.data:
                if isinstance(row, dict):
                    values.append(row.get(field_key))
                elif isinstance(row, list) and idx < len(row):
                    values.append(row[idx])
                else:
                    values.append(None)
            
            if any(v is not None for v in values):
                df_data[column_name] = values
        
        df = pd.DataFrame(df_data)
        
        if 'time' in df.columns:
            df['time'] = pd.to_datetime(df['time'], unit='s')
        
        return df
        