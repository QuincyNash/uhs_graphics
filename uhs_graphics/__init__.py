__version__ = "0.0.54"
__KEY__ = "iZp6JK0WyW152Tqb68FxdkONgBKVG3G9"


from uhs_graphics._scene import Scene, MouseEvent
from uhs_graphics._vector import Vector
from uhs_graphics import objects
from uhs_graphics import color
import time


def rate(fps: int) -> None:
    time.sleep(1 / fps)
