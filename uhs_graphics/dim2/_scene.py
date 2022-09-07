from __future__ import annotations
import gc
import json
import time
from typing import List

from uhs_graphics import __KEY__
from ._object import Object
from ._vector import Vector


class MouseEvent:
    def __init__(self, *, x: int, y: int) -> None:
        self.x = x
        self.y = y


class KeyboardEvent:
    def __init__(self, *, key: str, key_code: int, shift: bool, ctrl: bool, alt: bool, meta: bool) -> None:
        self.key = key
        self.key_code = key_code
        self.shift = shift
        self.ctrl = ctrl
        self.meta = meta
        self.alt = alt


class Scene:
    _instances: List[Scene] = []

    def __init__(self, width: int, height: int) -> None:
        if len(self.__class__._instances) == 0:
            self.__class__._instances.append(self)
        else:
            raise Exception("A scene has already been instantiated")

        self._width = width
        self._height = height
        self._objects: List[Object] = []
        self._events = {
            "mousedown": [],
            "mouseup": [],
            "keydown": [],
            "keyup": [],
        }
        self._mouse_pos = Vector(0, 0)
        self._keys_pressed: List[str] = []
        print(self._descriptor())

    @ property
    def width(self) -> int:
        return self._width

    @ width.setter
    def width(self, width: int) -> int:
        self._width = width
        return self._width

    @ property
    def height(self) -> int:
        return self._height

    @ height.setter
    def set_height(self, height: int) -> int:
        self._height = height
        return self._height

    def bind(self, event: str, func: function) -> Scene:
        if isinstance(self._events.get(event), list):
            self._events[event].append(func)
        else:
            raise Exception(f"The event '{event}' does not exist")
        return self

    def _trigger(self, event: str, data) -> None:
        if event == "keydown":
            self._keys_pressed.append(data.key)
        elif event == "keyup":
            if data.key in self._keys_pressed:
                self._keys_pressed.remove(data.key)

        for ev in self._events[event]:
            ev(data)

    def _descriptor(self) -> str:
        data = json.dumps({
            "timestamp": time.time(),
            "type": "2d",
            "size": {
                "x": self._width,
                "y": self._height
            }
        })

        return f"{__KEY__} {data}"
