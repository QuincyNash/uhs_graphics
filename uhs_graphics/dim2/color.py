import colorsys


def hsv(hue: int, saturation: int, value: int):
    r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation / 100, value / 100)
    return Color(int(r * 255), int(g * 255), int(b * 255))


def rgb(red: int, green: int, blue: int):
    return Color(red, green, blue)


class Color:
    def __init__(self, r: int, g: int, b: int, *, _internal_flags: dict = {}) -> None:
        self._r = r
        self._g = g
        self._b = b
        self._on_change: function = _internal_flags.get(
            "_on_change", lambda: None)

    def __str__(self) -> str:
        return f"Color < {self._r} {self._g} {self._b} >"

    def __repr__(self) -> str:
        return f"color {self._r},{self._g},{self._b}"

    @property
    def r(self) -> int:
        return self._r

    @r.setter
    def r(self, r: int) -> int:
        self._r = r
        self._on_change()
        return self._r

    @property
    def g(self) -> int:
        return self._g

    @g.setter
    def g(self, g: int) -> int:
        self._g = g
        self._on_change()
        return self._g

    @property
    def b(self) -> int:
        return self._b

    @b.setter
    def b(self, b: int) -> int:
        self._b = b
        self._on_change()
        return self._b
