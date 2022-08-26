from typing import List
from ._object import Object

_KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Scene:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._objects: List[Object] = []

    def _get_objects(self):
        return map(lambda x: x.__str__(), self._objects)

    def _generate_frame(self):
        print(_KEY, *self._get_objects())

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
