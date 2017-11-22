from coord import Coord
from numpy import random as r


class Trajectory(object):

    def __init__(self, point: Coord, k: float, step: float, size: int) -> None:
        self._point = point
        self._k = k
        self._step = step
        self._size = size

    @property
    def k(self) -> float:
        return self._k

    @property
    def step(self) -> float:
        return self._step

    @property
    def size(self) -> int:
        return self._size

    def generate_linear_trajectory(self):
        x = [self._point.x]
        y = [self._point.y]

        for i in range(1, self._size):
            x.append(x[i - 1] + self._step)
            y.append(self._k * x[i] + r.random())

        return x, y
