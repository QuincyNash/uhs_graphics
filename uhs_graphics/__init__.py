__version__ = "0.0.73"
__KEY__ = "iZp6JK0WyW152Tqb68FxdkONgBKVG3G9"


from uhs_graphics._scene import Scene, MouseEvent
from uhs_graphics._vector import Vector
from uhs_graphics import objects
from uhs_graphics import color


def rate(fps: int) -> None:
    import time
    time.sleep(1 / fps)


def wait_for_events() -> None:
    while True:
        rate(1)
