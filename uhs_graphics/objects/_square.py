from .._object import Object
from .._vector import Vector
from ..color import Color


class Square(Object):
    def __init__(self, x: int = 0, y: int = 0, width: int = 1, height: int = 1, *, color: Color = Color(255, 255, 255)) -> None:
        Object.__init__(self, x, y, color=color)
        self._size = Vector(width, height)
        self._calculate_points()

    def __str__(self) -> str:
        return f"objects.Square < {self._pos.x} {self._pos.y} {self._size.x} {self._size.y} >"

    def __repr__(self) -> str:
        return f"objects.Square(x={self._pos.x}, y={self._pos.y}, width={self._size.x}, height={self._size.y}, color={self._color.__repr__()})"

    @property
    def width(self) -> int:
        return self._size.x

    @width.setter
    def width(self, width: int) -> int:
        self._size.x = width
        self._calculate_points()
        return self._size.x

    @property
    def height(self) -> int:
        return self._size.y

    @height.setter
    def height(self, height: int) -> int:
        self._size.y = height
        self._calculate_points()
        return self._size.y

    @property
    def size(self) -> Vector:
        return self._size

    @size.setter
    def size(self, size: Vector) -> Vector:
        self._size = size
        self._calculate_points()
        return self._size

    def _calculate_points(self) -> None:
        p1 = Vector(self._pos.x - self._size.x / 2,
                    self._pos.y + self._size.y / 2)

        p2 = Vector(self._pos.x + self._size.x / 2,
                    self._pos.y + self._size.y / 2)

        p3 = Vector(self._pos.x + self._size.x / 2,
                    self._pos.y - self._size.y / 2)

        p4 = Vector(self._pos.x - self._size.x / 2,
                    self._pos.y - self._size.y / 2)

        self._points = [p1, p2, p3, p4]

        print(self._descriptor())
