from tetris.field import Tetris

tetris = Tetris()

while next(tetris).game:
    print(tetris)
    print()

