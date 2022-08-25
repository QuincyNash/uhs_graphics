class Vector:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x
        return self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y
        return self._y
