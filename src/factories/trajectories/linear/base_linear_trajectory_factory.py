from abc import abstractmethod

from typing import Generic, TypeVar, Type

S = TypeVar("State")
T = TypeVar("Trajectory")


class BaseLinearTrajectoryFactory(Generic[S, T]):

    def __init__(self, state: S, size: int, trajectory: Type[T]):
        """        
        :param state: начальный вектор состояния 
        :param size: количество отметок траектории
        """
        self._size = size
        self._state = state
        self._trajectory = trajectory

    @abstractmethod
    def next(self, last: S) -> S:
        raise NotImplementedError

    def create(self) -> T:
        trajectory = self._trajectory()  # type: ignore
        trajectory.append(self._state)

        for i in range(self._size):
            trajectory.append(self.next(trajectory.last))

        return trajectory

