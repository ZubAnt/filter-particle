import numpy as np

from src.models.trajectories.linear.linear_trajectory_1d import LinearTrajectory1D
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D


class MeasureLinear1DFactory(object):

    def __init__(self, trajectory: LinearTrajectory1D, dv: float):
        self._trajectory = trajectory
        self._vectors = trajectory.vectors
        self._dv = dv

    def create(self) -> LinearTrajectory1D:
        measurements = LinearTrajectory1D()
        for s in self._trajectory.vectors:
            state = StateVectorLinear1D(s.time, s.value + np.random.uniform(s.value - self._dv, s.value + self._dv))
            measurements.append(state)

        return measurements
