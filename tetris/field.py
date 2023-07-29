import random
import numpy as np
from tetris.consts import RED, GREEN
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
        self.AI_color: tuple[int, int, int] = RED

        self.figure: Figure = None
        self.figure_xs: np.array = None
        self.figure_ys: np.array = None
        self.figures_colors = set()

        self.put_new_figure()

        self.score = 0

    def __str__(self):
        return "\n".join(["".join(str(i)) for i in self.window[-20:]])

    def __next__(self):
        if np.any(self.figure_ys == self.WINDOW[0] - 1) or np.any(
                ((elems_below_than_figure := self.window[self.figure_ys + 1, self.figure_xs]) != Tetris.EMPTY) &
                (elems_below_than_figure != self.figure.number_of_color)
        ):
            self.put_new_figure()
            self.check_rows()
        else:
            self.update(True)
        return self

    def put_new_figure(self) -> None:
        self.figure = random.choice(self.figures)()
        self.figures_colors.add(self.figure.number_of_color)
        self.figure_xs, self.figure_ys = self.figure.rotate(random.choice((-1, 1)))

        for i in range(random.randint(1, 4)):
            self.rotate(-1)
        self.figure_xs += 4

        if any(self.window[self.figure_ys, self.figure_xs] != Tetris.EMPTY):
            self.game_over()

    def check_rows(self) -> None:
        for i, row in enumerate(self.window):
            if np.all(row != 0):
                self.score += i
                self.window[1:i + 1] = self.window[:i]

    def event(self, _event):
        match _event:
            case "LEFT":
                self.move(-1)
            case "RIGHT":
                self.move(1)
            case "ROTATE_CW":
                self.rotate(-1)
            case "ROTATE_CCW":
                self.rotate(1)
            case "SWITCH_AI":
                self.switch_AI()
        self.update(False)

    def update(self, _update_y=False):
        self.window[self.window == self.figure.number_of_color] = Tetris.EMPTY
        if _update_y:
            self.figure_ys += 1
        self.window[self.figure_ys, self.figure_xs] = self.figure.number_of_color

    def move(self, direction):
        wall = (np.all(self.figure_xs < Tetris.WINDOW[1] - 1) and
                direction == 1) or \
               (np.all(self.figure_xs > 0) and
                direction == -1)
        figure = False

        if wall:
            figure1 = (__direction := self.window[
                self.figure_ys, self.figure_xs + direction
            ]) == Tetris.EMPTY
            figure2 = __direction == self.figure.number_of_color

            figure = np.all(figure1 | figure2)

        if wall and figure:
            self.figure_xs += direction

    def rotate(self, direction):
        # TODO: the figure should not rotate if a part of another figure is destroyed at the same time.
        _y = np.min(self.figure_ys)
        _x = np.min(self.figure_xs)

        self.figure_xs, self.figure_ys = self.figure.rotate(direction)
        self.figure_xs += _x
        self.figure_ys += _y

        if np.any(self.figure_xs < 1):
            self.figure_xs -= np.min(self.figure_xs)
        if np.any(self.figure_xs >= self.WINDOW[1]):
            self.figure_xs -= np.max(self.figure_xs) - self.WINDOW[1] + 1

    def switch_AI(self):
        self.AI_color = RED if self.AI_color == GREEN else GREEN
        # TODO: Connect an AI that will play by itself

    def game_over(self) -> None:
        self.game = False
        print(Tetris.GAME_OVER_MESSAGE.format(self.score))
