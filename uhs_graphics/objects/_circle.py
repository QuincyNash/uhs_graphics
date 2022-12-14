from typing import Union
from .._object import Object
from ..color import Color
from ._ellipse import Ellipse


class Circle(Ellipse):
    def __init__(self, x: int = 0, y: int = 0, radius: int = 0.5, *, color: Color = Color(0, 0, 0), border: Union[Color, None] = None, border_thickness: int = 1, fixed: bool = False, layer: int = None) -> None:
        Ellipse.__init__(self, x, y, radius, radius,
                         color=color, border=border,
                         border_thickness=border_thickness, fixed=fixed, layer=layer)
        self._radius = radius
        self._calculate_points()

    def __str__(self) -> str:
        return f"objects.Circle < {self._pos._x} {self._pos._y} {self._radius} >"

    def __repr__(self) -> str:
        return f"objects.Circle(x={self._pos._x}, y={self._pos._y}, radius={self._radius}, color={self._color.__repr__()}, fixed={self._fixed}, layer={self._layer})"

    @property
    def r(self) -> int:
        return self._radius

    @r.setter
    def r(self, radius: int) -> int:
        self._radius = radius
        self._rx = radius
        self._ry = radius
        self._calculate_points()
        return self._radius

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, radius: int) -> int:
        self._radius = radius
        self._rx = radius
        self._ry = radius
        self._calculate_points()
        return self._radius
