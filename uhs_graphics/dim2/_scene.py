import json
import time
from typing import List

from uhs_graphics import __KEY__
from ._object import Object


class Scene:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._objects: List[Object] = []
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
