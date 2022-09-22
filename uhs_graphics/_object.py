from typing import List, Union
import uuid
import time
import json

from uhs_graphics import __KEY__
from ._vector import Vector
from .color import Color, rgb


class Object:
    _instance_count = 0

    def __init__(self, x: int = 0, y: int = 0, *, color: Color = rgb(0, 0, 0), border: Union[Color, None] = None, border_thickness: int = 1, fixed: bool = False, layer: int = Union[int, None]) -> None:
        self._id = uuid.uuid4()

        self._pos = Vector(x, y, _internal_flags={
            "_on_change": self._calculate_points})
        self._points: List[Vector] = []

        self._color = Color(color._r, color._g, color._b, _internal_flags={
                            "_on_change": self._calculate_points})
        self._border = Color(border._r, border._g, border._b, _internal_flags={
            "_on_change": self._calculate_points}) if border is not None else None
        self._border_thickness = border_thickness

        self._fixed = fixed
        if layer is None:
            self._layer = Object._instance_count
            Object._instance_count += 1
        else:
            self._layer = layer

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
        self._pos._x = pos._x
        self._pos._y = pos._y
        self._calculate_points()
        return self._pos

    @property
    def position(self) -> Vector:
        return self._pos

    @position.setter
    def position(self, pos: Vector) -> Vector:
        self._pos._x = pos._x
        self._pos._y = pos._y
        self._calculate_points()
        return self._pos

    @property
    def fixed(self) -> bool:
        return self._fixed

    @fixed.setter
    def fixed(self, fixed: bool) -> bool:
        self._fixed = fixed
        self._calculate_points()
        return self._fixed

    @property
    def layer(self) -> int:
        return self._layer

    @layer.setter
    def layer(self, layer: int) -> int:
        self._layer = layer
        self._calculate_points()
        return self._layer

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, color: Color) -> Color:
        self._color.set(color._r, color._g, color._b)
        self._calculate_points()
        return self._color

    @property
    def border(self) -> Union[Color, None]:
        return self._border

    @border.setter
    def border(self, border: Union[Color, None]) -> Union[Color, None]:
        if border is None:
            self._border = None
        elif self._border is None:
            self._border = Color(border._r, border._g, border._b)
        else:
            self._border.set(border._r, border._g, border._b)

        self._calculate_points()
        return self._border

    @property
    def border_thickness(self) -> int:
        return self._border_thickness

    @border_thickness.setter
    def border_thickness(self, border_thickness: int) -> int:
        self._border_thickness = border_thickness
        self._calculate_points()
        return self._border_thickness

    def _calculate_points(self) -> None:
        pass

    def _descriptor(self) -> str:
        data = json.dumps({
            "timestamp": time.time(),
            "id": str(self._id),
            "points": list(map(lambda p: p._descriptor(), self._points)),
            "color": self._color._descriptor(),
            "border": self._border._descriptor() if self._border is not None else "{}",
            "border_thickness": self._border_thickness,
            "fixed": self._fixed,
            "layer": self._layer
        })

        return f"{__KEY__} {data}"
