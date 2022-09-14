from __future__ import annotations
import json
import time
from typing import List

from uhs_graphics import __KEY__
from .color import Color
from ._object import Object
from ._vector import Vector


class MouseEvent:
    def __init__(self, *, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"MouseEvent(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"< {self.x} {self.y} >"


class KeyboardEvent:
    def __init__(self, *, key: str, key_code: str, shift: bool, ctrl: bool, alt: bool, meta: bool) -> None:
        self.key = key
        self.key_code = key_code
        self.shift = shift
        self.ctrl = ctrl
        self.meta = meta
        self.alt = alt

    def __repr__(self) -> str:
        return f"KeyboardEvent(key=\"{self.key}\", key_code=\"{self.key_code}\", shift={self.shift}, alt={self.alt}, ctrl={self.ctrl}, meta={self.meta})"

    def __str__(self) -> str:
        return self.key


class Scene:
    _instances: List[Scene] = []

    def __init__(self, width: int, height: int) -> None:
        if len(self.__class__._instances) == 0:
            self.__class__._instances.append(self)
        else:
            raise Exception("A scene has already been instantiated")

        self._width = width
        self._height = height
        self._objects: List[Object] = []
        self._bg = Color(255, 255, 255, _internal_flags={
            "_on_change": self._descriptor})
        self._events = {
            "mousedown": [],
            "mouseup": [],
            "keydown": [],
            "keyup": [],
        }
        self._mouse_pos = Vector(0, 0)
        self._keys_pressed: List[KeyboardEvent] = []
        self._descriptor()

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> int:
        self._width = width
        self._descriptor()
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> int:
        self._height = height
        self._descriptor()
        return self._height

    @property
    def bg(self) -> Color:
        return self._bg

    @bg.setter
    def bg(self, bg: Color) -> Color:
        self._bg.set(bg._r, bg._g, bg._b)
        self._descriptor()
        return self._bg

    @property
    def background(self) -> Color:
        return self._bg

    @background.setter
    def background(self, bg: Color) -> Color:
        self._bg.set(bg._r, bg._g, bg._b)
        self._descriptor()
        return self._bg

    def keys_pressed(self) -> List[str]:
        return [pressed.key_code for pressed in self._keys_pressed]

    def is_pressed(self, *keys: str) -> bool:
        return all([any(lambda pressed: pressed.key_code == key, self._keys_pressed) for key in keys])

    def bind(self, event: str, func: function) -> Scene:
        if isinstance(self._events.get(event), list):
            self._events[event].append(func)
        else:
            raise Exception(f"The event '{event}' does not exist")
        return self

    def _trigger(self, event: str, data: KeyboardEvent) -> None:
        if event == "keydown":
            self._keys_pressed.append(data)
        elif event == "keyup":
            self._keys_pressed = list(filter(
                lambda pressed: pressed.key != data.key or pressed.key_code != data.key_code or pressed.shift != data.shift or pressed.alt != data.alt or pressed.ctrl != data.ctrl or pressed.meta != data.meta, self._keys_pressed
            ))
        elif event == "releaseall":
            for pressed in self._keys_pressed:
                for ev in self._events["keyup"]:
                    ev(pressed)
            self._keys_pressed = []
            return None

        for ev in self._events[event]:
            ev(data)

    def _descriptor(self) -> None:
        data = json.dumps({
            "timestamp": time.time(),
            "bg": {
                "r": self._bg._r,
                "g": self._bg._g,
                "b": self._bg._b
            },
            "size": {
                "x": self._width,
                "y": self._height
            }
        })

        print(f"{__KEY__} {data}")
