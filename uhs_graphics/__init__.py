__version__ = "0.0.26"
__KEY__ = "iZp6JK0WyW152Tqb68FxdkONgBKVG3G9"


from ._scene import Scene
from ._vector import Vector
from . import objects
from . import color
import time


def rate(fps: int) -> None:
    time.sleep(1 / fps)
