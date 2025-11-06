# ObjectPool.py
import weakref
import threading
import time
from typing import Any, Optional, Callable, Dict
from collections import defaultdict
import logging
from .TVBridgeObject import TVMethodCall, TVMethodResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TVObjectPool:
    _instance: Optional['TVObjectPool'] = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init()
        return cls._instance

    def __del__(self):
        if self.cleanup_timer is not None and self.cleanup_timer.is_alive():
            self.cleanup_timer.cancel()
            self.cleanup_timer = None
            print("cleanup_timer")
        else:
            print("not running")

    def _init(self):
        self._object_to_id: Dict[int, str] = {}
        self._id_to_strongref: Dict[str, object] = {}
        self._id_to_obj_id: Dict[str, int] = {}
        self._on_object_released: Optional[Callable[[str], None]] = None
        self.cleanup_timer: Optional[threading.Timer] = threading.Timer(60, self.cleanup)
        self.start_cleanup_timer()

    @classmethod
    def get_instance(cls) -> 'TVObjectPool':
        return cls()
    
    def start_cleanup_timer(self):
        if self.cleanup_timer is not None:
            self.cleanup_timer.start()

    def register_object_with_id(self, obj: Any, obj_id_str: str, update: bool = False) -> str:
        if not isinstance(obj, object) or obj is None:
            raise TypeError("ObjectPool: can only register non-None objects")

        current_obj_id = id(obj)
        if not update:
            if current_obj_id in self._object_to_id:
                existing = self._object_to_id[current_obj_id]
                raise ValueError(f"ObjectPool: object already registered with ID {existing}")
            if obj_id_str in self._id_to_strongref:
                raise ValueError(f"ObjectPool: ID {obj_id_str} already in use")

        self._register_internal(obj, obj_id_str)
        return obj_id_str

    def _register_internal(self, obj: Any, obj_id_str: str) -> None:
        obj_id = id(obj)
        self._object_to_id[obj_id] = obj_id_str
        self._id_to_obj_id[obj_id_str] = obj_id

        self._id_to_strongref[obj_id_str] = obj

    def get_object_with_id(self, obj_id_str: str) -> Optional[Any]:
        obj = self._id_to_strongref.get(obj_id_str)
        
        if obj is None:
            self._id_to_strongref.pop(obj_id_str, None)
            self._id_to_obj_id.pop(obj_id_str, None)
            return None
        return obj

    def get_id_with_object(self, obj: Any) -> Optional[str]:
        if obj is None:
            return None
        return self._object_to_id.get(id(obj))

    def has_id(self, obj_id_str: str) -> bool:
        return self.get_object_with_id(obj_id_str) is not None

    def release(self, obj_id_str: str) -> None:
        obj = self.get_object_with_id(obj_id_str)
        if obj is not None:
            obj_id = id(obj)
            self._object_to_id.pop(obj_id, None)
        self._id_to_strongref.pop(obj_id_str, None)
        self._id_to_obj_id.pop(obj_id_str, None)

    def on(self, event: str, callback: Callable[[str], None]) -> None:
        if event == "objectReleased" and callable(callback):
            self._on_object_released = callback
        else:
            raise ValueError(f"Unsupported event: {event}")

    
    def cleanup(self) -> None:
        to_remove = []
        for oid, obj in self._id_to_strongref.items():
            if obj is None:
                to_remove.append(oid)
        for oid in to_remove:
            self._id_to_strongref.pop(oid, None)
            self._id_to_obj_id.pop(oid, None)
        logging.debug(f"TVObjectPool Cleaned up: {self._id_to_strongref.items()}")
        self.cleanup_timer = threading.Timer(60, self.cleanup)
        self.start_cleanup_timer()

    def clear(self):
        self._object_to_id.clear()
        self._id_to_strongref.clear()
        self._id_to_obj_id.clear()

    def updateAliveObjects(self, aliveObjectIds: list[str]):
        to_remove = []
        for oid in self._id_to_strongref.keys():
            if oid not in aliveObjectIds:
                to_remove.append(oid)
            else:
                pass
            
        for oid in to_remove:
            self.release(oid)
    def remoteObjectReleased(self, objectId: str):
        self.release(objectId)

    def handle_remote_call(self, callParams: TVMethodCall):
        if callParams.method_name == "updateAliveObjects":
            self.updateAliveObjects(**callParams.kwargs)
        elif callParams.method_name == "remoteObjectReleased":
            self.remoteObjectReleased(**callParams.kwargs)
        else:
            pass

        resp = {"result": "success"}
        return resp

