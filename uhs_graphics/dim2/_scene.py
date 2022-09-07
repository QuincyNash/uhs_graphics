from __future__ import annotations
import gc
import json
import time
from typing import List

from uhs_graphics import __KEY__
from ._object import Object


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
            "mousedown": lambda: 0,
            "mouseup": lambda: 0,
        }
        print(self._descriptor())

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> int:
        self._width = width
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def set_height(self, height: int) -> int:
        self._height = height
        return self._height

    def bind(self, event: str, func: function) -> Scene:
        if self._events.get(event) is not None:
            self._events[event] = func
        return self

    def _trigger(self, event: str, data) -> None:
        self._events[event](data)

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
