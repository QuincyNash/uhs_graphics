from math import degrees, sin, cos
from .._object import Object
from .._vector import Vector
from ..color import Color


class Circle(Object):
    def __init__(self, x: int = 0, y: int = 0, radius: int = 0.5, *, color: Color = Color(255, 255, 255)) -> None:
        Object.__init__(self, x, y, color=color)
        self._radius = radius
        self._calculate_points()

    def __str__(self) -> str:
        return f"objects.Circle < {self._pos.x} {self._pos.y} {self._radius} >"

    def __repr__(self) -> str:
        return f"objects.Circle(x={self._pos.x}, y={self._pos.y}, radius={self._radius}, color={self._color.__repr__()})"

    @property
    def r(self) -> int:
        return self._radius

    @r.setter
    def r(self) -> int:
        return self._radius

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self) -> int:
        return self._radius

    def _calculate_points(self) -> None:
        self._points = []
        for angle in range(360):
            point = Vector(self._x + self._radius * cos(degrees(angle)),
                           self._y + self._radius * sin(degrees(angle)))

            self._points.append(point)

        print(self._descriptor())
