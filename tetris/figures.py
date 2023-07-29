from abc import ABC
import numpy as np


class Figure(ABC):
    __count = 0

    def __init__(self):
        self.xyz = None
        self._xyz = None
        Figure.__count += 1
        self.number_of_color = Figure.__count
        self._rotate = 0

    def rotate(self, way: int) -> np.array:
        self._rotate += way

        self._rotate %= len(self._xyz)
        self.xyz = self._xyz[self._rotate]
        param = np.array(self.xyz[0]), np.array(self.xyz[1])
        return param


class O(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((0, 0, 1, 1), (0, 1, 0, 1)),)

    def rotate(self, way: int) -> np.array:
        self.xyz = self._xyz[self._rotate]
        return np.array(self.xyz[0]), np.array(self.xyz[1])


class I(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((0, 1, 2, 3), (0, 0, 0, 0)),
                     ((0, 0, 0, 0), (0, 1, 2, 3)))


class J(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((0, 1, 2, 2), (1, 1, 0, 1)),
                     ((1, 1, 1, 0), (0, 1, 2, 0)),
                     ((0, 0, 1, 2), (0, 1, 0, 0)),
                     ((0, 0, 0, 1), (0, 1, 2, 2)))


class L(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((0, 1, 2, 2), (0, 0, 0, 1)),
                     ((1, 1, 1, 0), (0, 1, 2, 2)),
                     ((0, 0, 1, 2), (0, 1, 1, 1)),
                     ((0, 0, 0, 1), (0, 1, 2, 0)))


class T(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((0, 1, 1, 1), (1, 0, 1, 2)),
                     ((1, 0, 1, 2), (0, 1, 1, 1)),
                     ((0, 0, 0, 1), (0, 1, 2, 1)),
                     ((0, 1, 2, 1), (0, 0, 0, 1)))


class Z(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((0, 0, 1, 1), (0, 1, 1, 2)),
                     ((1, 2, 0, 1), (0, 0, 1, 1)))


class S(Figure):
    def __init__(self):
        super().__init__()
        self._xyz = (((1, 1, 0, 0), (0, 1, 1, 2)),
                     ((0, 1, 1, 2), (0, 0, 1, 1)))
