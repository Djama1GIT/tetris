import random
import numpy as np
from figures import Square


class Tetris:
    figures = [
        Square,
    ]

    def __init__(self):
        self.window = np.empty((24, 10), dtype=object)
        self.window[:] = "□ "
        self.point = [4, 0]

    def __str__(self):
        return "\n".join(["".join(i) for i in self.window[-20:]])

    def __next__(self):
        self.window[*self.point] = "▅ "
        self.point = [self.point[0], self.point[1] + 1]
        return self

    def put(self):
        """Put figure"""
        random.choice(self.figures)
