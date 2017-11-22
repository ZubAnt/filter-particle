from src.factories.trajectories.linear.base_linear_trajectory_factory import BaseLinearTrajectoryFactory
from src.models.trajectories.linear.linear_trajectory_1d import LinearTrajectory1D
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D


class LinearTrajectory1DFactory(BaseLinearTrajectoryFactory[StateVectorLinear1D, LinearTrajectory1D]):

    def __init__(self, state: StateVectorLinear1D, size: int, k: float, dt: float) -> None:
        super().__init__(state, size, LinearTrajectory1D)
        self._k = k
        self._dt = dt
        self._dv = self._k * self._dt

    def next(self, last: StateVectorLinear1D):
        return StateVectorLinear1D(last.time + self._dt, last.value + self._dv)
