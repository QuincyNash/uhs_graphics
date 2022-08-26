__version__ = "0.0.1"

from dim2 import *

square = objects.Square(0, 0, 10, 15, color=color.rgb(0, 0, 0))
square.r = 0

print(square._descriptor())
