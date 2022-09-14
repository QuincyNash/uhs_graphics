from math import radians, sin, cos
from .._object import Object
from .._vector import Vector
from ..color import Color


class Ellipse(Object):
    def __init__(self, x: int = 0, y: int = 0, rx: int = 1, ry: int = 0.5, *, color: Color = Color(0, 0, 0)) -> None:
        Object.__init__(self, x, y, color=color)
        self._rx = rx
        self._ry = ry
        self._calculate_points()

    def __str__(self) -> str:
        return f"objects.Ellipse < {self._pos._x} {self._pos._y} {self._rx} {self._ry} >"

    def __repr__(self) -> str:
        return f"objects.Circle(x={self._pos._x}, y={self._pos._y}, rx={self._rx}, ry={self._ry}, color={self._color.__repr__()})"

    @property
    def rx(self) -> int:
        return self._rx

    @rx.setter
    def rx(self, rx: int) -> int:
        self._rx = rx
        self._calculate_points()
        return self._rx

    @property
    def ry(self) -> int:
        return self._ry

    @ry.setter
    def ry(self, ry: int) -> int:
        self._ry = ry
        self._calculate_points()
        return self._ry

    def _calculate_points(self) -> None:
        self._points = []
        for angle in range(0, 360):
            point = Vector(self._pos._x + self._rx * cos(radians(angle)),
                           self._pos._y + self._ry * sin(radians(angle)))
            self._points.append(point)

        print(self._descriptor())
