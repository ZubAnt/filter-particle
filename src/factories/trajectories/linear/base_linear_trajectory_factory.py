from abc import abstractmethod

from typing import Generic, TypeVar

from src.models.trajectories.linear.base_linear_trajectory import BaseLinearTrajectory
S = TypeVar("State")


class BaseLinearTrajectoryFactory(Generic[S]):

    def __init__(self, state: S, size: int):
        """        
        :param state: начальный вектор состояния 
        :param size: количество отметок траектории
        """
        self._size = size
        self._state = state

    # @property
    # @abstractmethod
    # def next(self, last: S) -> S:
    #     raise NotImplementedError

    @abstractmethod
    def next(self, last: S) -> S:
        raise NotImplementedError

    def create(self) -> BaseLinearTrajectory:
        trajectory = BaseLinearTrajectory()
        trajectory.append(self._state)

        for i in range(self._size):
            trajectory.append(self.next(trajectory.last))

        return trajectory

