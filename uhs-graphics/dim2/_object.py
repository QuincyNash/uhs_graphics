from ._vector import Vector


class Object:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._pos = Vector(x, y)

    @property
    def x(self) -> int:
        return self._pos.x

    @x.setter
    def x(self, x: int) -> int:
        self._pos.x = x
        return self._pos.x

    @property
    def y(self) -> int:
        return self._pos.y

    @y.setter
    def y(self, y: int) -> int:
        self._pos.y = y
        return self._pos.y

    @property
    def pos(self):
        return self._pos

    @ pos.setter
    def pos(self, pos: Vector):
        self._pos = pos
        return self._pos
