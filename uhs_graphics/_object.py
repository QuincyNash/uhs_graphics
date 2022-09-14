from typing import List
import uuid
import time
import json

from uhs_graphics import __KEY__
from ._vector import Vector
from .color import Color, rgb


class Object:
    def __init__(self, x: int = 0, y: int = 0, *, color: Color = rgb(0, 0, 0)) -> None:
        self._id = uuid.uuid4()
        self._pos = Vector(x, y, _internal_flags={
            "_on_change": self._calculate_points})
        self._points: List[Vector] = []
        self._color = Color(color._r, color._g, color._b, _internal_flags={
                            "_on_change": self._calculate_points})

    @property
    def x(self) -> int:
        return self._pos._x

    @x.setter
    def x(self, x: int) -> int:
        self._pos._x = x
        self._calculate_points()
        return self._pos._x

    @property
    def y(self) -> int:
        return self._pos._y

    @y.setter
    def y(self, y: int) -> int:
        self._pos._y = y
        self._calculate_points()
        return self._pos._y

    @property
    def pos(self) -> Vector:
        return self._pos

    @pos.setter
    def pos(self, pos: Vector) -> Vector:
        self._pos = pos
        self._calculate_points()
        return self._pos

    @property
    def position(self) -> Vector:
        return self._pos

    @position.setter
    def position(self, pos: Vector) -> Vector:
        self._pos = pos
        self._calculate_points()
        return self._pos

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, color: Color) -> Color:
        self._color.set(color._r, color._g, color._b)
        self._calculate_points()
        return self._color

    def _calculate_points(self) -> None:
        pass

    def _descriptor(self) -> str:
        data = json.dumps({
            "timestamp": time.time(),
            "id": str(self._id),
            "points": list(map(lambda p: p._descriptor(), self._points)),
            "color": self._color._descriptor()
        })

        return f"{__KEY__} {data}"
