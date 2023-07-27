from abc import ABC, abstractmethod
from random import randint


class Figure(ABC):
    __count = 0

    def __init__(self):
        self.pos = self.xyz
        Figure.__count += 1
        self.color = Figure.__count

    @property
    @abstractmethod
    def xyz(self) -> list[tuple]:
        raise NotImplementedError

    def rotate(self, way: int) -> list[tuple]:
        match way:
            case 0:
                # 0 degrees
                self.pos = self.xyz
            case 1:
                # 90 degrees
                self.pos = [(x, y) for y, x in self.xyz]
            case 2:
                # 180 degrees
                maximum_y = max([y for y, x in self.xyz])
                self.pos = [(maximum_y - y, x) for y, x in self.xyz]
            case 3:
                # 270 degrees
                maximum_x = max([x for x, y in self.xyz])
                self.pos = [(y, maximum_x - x) for x, y in self.xyz]
        return self.pos


class O(Figure):
    @property
    def xyz(self):
        return [
            (0, 0), (0, 1),
            (1, 0), (1, 1)
        ]


class I(Figure):
    @property
    def xyz(self):
        return [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        ]


class J(Figure):
    @property
    def xyz(self):
        return [
                    (0, 1),
                    (1, 1),
            (2, 0), (2, 1),
        ]


class L(Figure):
    @property
    def xyz(self):
        return [
            (0, 0),
            (1, 0),
            (2, 0), (2, 1),
        ]


class Z(Figure):
    @property
    def xyz(self):
        return [
            (0, 0), (0, 1),
                    (1, 1), (1, 2),
        ]


class T(Figure):
    @property
    def xyz(self):
        return [
                    (0, 1),
            (1, 0), (1, 1), (1, 2),
        ]


class S(Figure):
    @property
    def xyz(self):
        return [
                    (0, 1), (0, 2),
            (1, 0), (1, 1),
        ]

