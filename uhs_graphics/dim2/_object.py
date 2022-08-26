from typing import List
from ._vector import Vector
from .color import Color, rgb

_KEY = "abcdefghijklmnopqrstuvwxyz"


class Object:
    def __init__(self, x: int = 0, y: int = 0, *, color: Color = rgb(255, 255, 255)) -> None:
        self._pos = Vector(x, y, _internal_flags={
            "_on_change": self._calculate_points})
        self._points: List[Vector] = []
        self._color = Color(color._r, color._g, color._b, _internal_flags={
                            "_on_change": self._calculate_points})

    @property
    def x(self) -> int:
        return self._pos.x

    @x.setter
    def x(self, x: int) -> int:
        self._pos.x = x
        self._calculate_points()
        return self._pos.x

    @property
    def y(self) -> int:
        return self._pos.y

    @y.setter
    def y(self, y: int) -> int:
        self._pos.y = y
        self._calculate_points()
        return self._pos.y

    @property
    def pos(self) -> Vector:
        return self._pos

    @pos.setter
    def pos(self, pos: Vector) -> Vector:
        self._pos = pos
        self._calculate_points()
        return self._pos

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, color: Color) -> Color:
        self._color = color
        return self._color

    def _calculate_points(self) -> None:
        pass

    def _descriptor(self) -> str:
        return f"{_KEY} | object2d | {' '.join(map(lambda p: p.__repr__(), self._points))} | {self._color.__repr__()}"
