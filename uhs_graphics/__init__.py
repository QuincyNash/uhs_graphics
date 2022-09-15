__version__ = "0.0.49"
__KEY__ = "iZp6JK0WyW152Tqb68FxdkONgBKVG3G9"


from uhs_graphics._scene import Scene, MouseEvent
from uhs_graphics._vector import Vector
from uhs_graphics import objects
from uhs_graphics import color
import time


def rate(fps: int) -> None:
    time.sleep(1 / fps)


scene = Scene(100, 100)
scene.bind("mousedown", lambda a, b: print("DOWN"))
scene.bind("mouseup", lambda a, b: print("UP"))

scene._trigger("mousedown", MouseEvent(x=5, y=5))
scene._trigger("mouseup", MouseEvent(x=5, y=5))
