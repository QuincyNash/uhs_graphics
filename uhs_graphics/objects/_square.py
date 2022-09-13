from .._object import Object
from .._vector import Vector
from ..color import Color


class Square(Object):
    def __init__(self, x: int = 0, y: int = 0, width: int = 1, height: int = 1, *, color: Color = Color(0, 0, 0)) -> None:
        Object.__init__(self, x, y, color=color)
        self._size = Vector(width, height)
        self._calculate_points()

    def __str__(self) -> str:
        return f"objects.Square < {self._pos._x} {self._pos._y} {self._size._x} {self._size._y} >"

    def __repr__(self) -> str:
        return f"objects.Square(x={self._pos._x}, y={self._pos._y}, width={self._size._x}, height={self._size._y}, color={self._color.__repr__()})"

    @property
    def width(self) -> int:
        return self._size._x

    @width.setter
    def width(self, width: int) -> int:
        self._size._x = width
        self._calculate_points()
        return self._size._x

    @property
    def height(self) -> int:
        return self._size._y

    @height.setter
    def height(self, height: int) -> int:
        self._size._y = height
        self._calculate_points()
        return self._size._y

    @property
    def size(self) -> Vector:
        return self._size

    @size.setter
    def size(self, size: Vector) -> Vector:
        self._size = size
        self._calculate_points()
        return self._size

    def _calculate_points(self) -> None:
        p1 = Vector(self._pos._x - self._size._x / 2,
                    self._pos._y + self._size._y / 2)

        p2 = Vector(self._pos._x + self._size._x / 2,
                    self._pos._y + self._size._y / 2)

        p3 = Vector(self._pos._x + self._size._x / 2,
                    self._pos._y - self._size._y / 2)

        p4 = Vector(self._pos._x - self._size._x / 2,
                    self._pos._y - self._size._y / 2)

        self._points = [p1, p2, p3, p4]

        print(self._descriptor())
