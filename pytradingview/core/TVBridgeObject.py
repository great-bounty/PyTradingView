from typing import Callable, Dict, Any, Optional

class TVMethodCall:
    def __init__(
        self,
        *,
        class_name: Optional[str] = None,
        object_id: Optional[str] = None,
        method_name: str,
        kwargs: Optional[Dict[str, Any]] = None
    ):
        self.object_id = object_id
        self.class_name = class_name
        self.method_name = method_name
        self.kwargs = kwargs or {}

    def to_json(self) -> dict:
        return {
            "objectId": self.object_id,
            "className": self.class_name,
            "methodName": self.method_name,
            "kwargs": self.kwargs
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TVMethodCall":
        return cls(
            object_id=data.get("objectId"),
            class_name=data.get("className"),
            method_name=data["methodName"],
            kwargs=data.get("kwargs", {})
        )

    def __repr__(self):
        target = self.object_id or self.class_name or "global"
        return f"<TVMethodCall {target}.{self.method_name}({self._format_args()})>"

    def _format_args(self) -> str:
        parts = []
        if self.kwargs:
            parts.extend(f"{k}={v!r}" for k, v in self.kwargs.items())
        return ", ".join(parts)
    

class TVMethodResponse:
    def __init__(
        self,
        *,
        result: Any = None,
        error: Optional[str] = None,
    ):
        self.result = result
        self.error = error

    @property
    def is_success(self) -> bool:
        return self.error is None

    def to_json(self) -> dict:
        d = {
            "result": self.result,
            "error": self.error
        }
        
        return d

    @classmethod
    def from_dict(cls, data: dict) -> "TVMethodResponse":
        return cls(
            result=data.get("result"),
            error=data.get("error")
        )

    def raise_if_error(self):
        if self.error:
            raise RuntimeError(f"Remote call failed: {self.error}")

    def __repr__(self):
        if self.error:
            return f"<TVMethodResponse ERROR: {self.error}>"
        else:
            return f"<TVMethodResponse result={self.result!r}>"