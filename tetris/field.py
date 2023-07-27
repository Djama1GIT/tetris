import random
import numpy as np
from tetris.figures import O, I, J, L, Z, T, S


class Tetris:
    EMPTY = 0
    WINDOW = (20 + 4, 10)
    figures = [O, I, J, L, Z, T, S]

    GAME_OVER_MESSAGE = "Game over! Your score: {0}"

    def __init__(self):
        self.window = np.empty(Tetris.WINDOW, dtype=object)
        self.window[:] = Tetris.EMPTY
        self.game = True

        self.figure = None
        self.figure_xs = None
        self.figure_ys = None
        self.figures_colors = set()

        self.put_new_figure()

        self.score = 0

    def __str__(self):
        return "\n".join(["".join(str(i)) for i in self.window[-20:]])

    def __next__(self):
        if np.any(
                self.figure_ys == self.WINDOW[0] - 1) or np.any(
            (self.window[self.figure_ys + 1, self.figure_xs] != Tetris.EMPTY) &
            (self.window[self.figure_ys + 1, self.figure_xs] != self.figure.color)
        ):  # Other figure (collision)
            self.put_new_figure()
        self.window[self.window == self.figure.color] = Tetris.EMPTY
        self.figure_ys += 1
        self.window[self.figure_ys, self.figure_xs] = self.figure.color
        return self

    def put_new_figure(self):
        self.figure = random.choice(self.figures)()
        self.figure.pos = self.figure.rotate(random.randint(0, 4))
        self.figures_colors.add(self.figure.color)

        self.figure_xs, self.figure_ys = np.array(list(zip(*self.figure.pos)))
        self.figure_xs += 4
        self.figure_ys += 1

        if any(self.window[self.figure_ys, self.figure_xs] != Tetris.EMPTY):
            self.game_over()

    def game_over(self):
        self.game = False
        print(Tetris.GAME_OVER_MESSAGE.format(self.score))
