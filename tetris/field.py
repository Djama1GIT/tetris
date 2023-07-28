import random
import numpy as np
from tetris.figures import Figure, O, I, J, L, Z, T, S


class Tetris:
    EMPTY = 0
    WINDOW = (20 + 4, 10)
    figures = [O, I, J, L, Z, T, S]

    GAME_OVER_MESSAGE = "Game over! Your score: {0}"

    def __init__(self):
        self.window: np.array = np.empty(Tetris.WINDOW, dtype=object)
        self.window[:] = Tetris.EMPTY
        self.game: bool = True

        self.figure: Figure = None
        self.figure_xs: np.array = None
        self.figure_ys: np.array = None
        self.figures_colors = set()

        self.put_new_figure()

        self.score = 0

    def __str__(self):
        return "\n".join(["".join(str(i)) for i in self.window[-20:]])

    def __next__(self):
        if np.any(
                self.figure_ys == self.WINDOW[0] - 1) or np.any(
            ((__elems_below_than_figure := self.window[self.figure_ys + 1, self.figure_xs]) != Tetris.EMPTY) &
            (__elems_below_than_figure != self.figure.color)
        ):
            self.put_new_figure()
        self.window[self.window == self.figure.color] = Tetris.EMPTY
        self.figure_ys += 1
        self.window[self.figure_ys, self.figure_xs] = self.figure.color
        return self

    def put_new_figure(self) -> None:
        self.figure = random.choice(self.figures)()
        self.figures_colors.add(self.figure.color)
        self.figure_xs, self.figure_ys = self.figure.rotate(random.choice((-1, 1)), param=self.figure.xyz)
        for i in range(random.randint(1, 4)):
            self.figure.rotate(-1, param=(self.figure_xs, self.figure_ys))
        self.figure_xs += 4

        if any(self.window[self.figure_ys, self.figure_xs] != Tetris.EMPTY):
            self.game_over()

    def event(self, _event):
        match _event:
            case "LEFT":
                if np.all(self.figure_xs > 0):
                    self.figure_xs -= 1
            case "RIGHT":
                if np.all(self.figure_xs < Tetris.WINDOW[1] - 1):
                    self.figure_xs += 1
            case "ROTATE_CCW":
                self.figure_xs, self.figure_ys = self.figure.rotate(-1, param=(self.figure_xs, self.figure_ys))
            case "ROTATE_CW":
                self.figure_xs, self.figure_ys = self.figure.rotate(1, param=(self.figure_xs, self.figure_ys))

    def game_over(self) -> None:
        self.game = False
        print(Tetris.GAME_OVER_MESSAGE.format(self.score))
