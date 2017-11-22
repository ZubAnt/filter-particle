from numpy import random as r
from typing import List

from src.models.trajectories.linear.base_linear_trajectory import BaseLinearTrajectory
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D


class Trajectory(object):

    def __init__(self, point: StateVectorLinear, k: float, step: float, size: int) -> None:
        """        
        :param point: StateVectorLinear - 
        :param k: 
        :param step: 
        :param size: 
        """
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


class LinearTrajectory1D(BaseLinearTrajectory):

    def __init__(self):
        super().__init__()

    @property
    def values(self) -> List[float]:
        return [vector.value for vector in self.vectors]

    @property
    def times(self) -> List[float]:
        return [vector.time for vector in self.vectors]
