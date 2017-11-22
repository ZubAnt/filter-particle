import numpy as np

from src.models.trajectories.linear.linear_trajectory_1d import LinearTrajectory1D
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D


class MeasureLinear1DFactory(object):

    def __init__(self, trajectory: LinearTrajectory1D, sigma_v: float):
        self._trajectory = trajectory
        self._vectors = trajectory.vectors
        self._sigmaV = sigma_v

    def create(self) -> LinearTrajectory1D:
        measurements = LinearTrajectory1D()
        for s in self._trajectory.vectors:
            new_val = np.random.normal(loc=s.value, scale=self._sigmaV)
            state = StateVectorLinear1D(s.time, new_val)
            measurements.append(state)

        return measurements
