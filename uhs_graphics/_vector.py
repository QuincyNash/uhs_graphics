from __future__ import annotations
import json


class Vector:
    def __init__(self, x: int, y: int, *, _internal_flags: dict = {}) -> None:
        self._x = x
        self._y = y
        self._on_change: function = _internal_flags.get(
            "_on_change", lambda: None)

    def __str__(self) -> str:
        return f"< {self._x} {self._y} >"

    def __repr__(self) -> str:
        return f"Vector(x={self._x}, y={self._y})"

    def descriptor(self) -> str:
        return json.dumps({
            "x": self._x,
            "y": self._y
        })

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> int:
        self._x = x
        self._on_change()
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> int:
        self._y = y
        self._on_change()
        return self._y

    def copy(self) -> Vector:
        return Vector(self._x, self._y)
