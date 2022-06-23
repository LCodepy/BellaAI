from __future__ import annotations

from typing import Tuple


class Color:

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = min(255, max(r, 0))
        self.g = min(255, max(g, 0))
        self.b = min(255, max(b, 0))

    # Functions

    @property
    def c(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    def brighter(self, value: int) -> Color:
        return Color(self.r + value, self.g + value, self.b + value)

    def darker(self, value: int) -> Color:
        return Color(self.r - value, self.g - value, self.b - value)


class Colors:

    white = Color(255, 255, 255)
    black = Color(0, 0, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 0, 255)
    yellow = Color(255, 255, 0)
    brown = Color(100, 60, 20)

