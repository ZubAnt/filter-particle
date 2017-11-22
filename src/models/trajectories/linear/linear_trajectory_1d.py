from typing import List

from src.models.trajectories.linear.base_linear_trajectory import BaseLinearTrajectory
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D
import matplotlib.pyplot as plt


class LinearTrajectory1D(BaseLinearTrajectory[StateVectorLinear1D]):

    def __init__(self):
        super().__init__()

    @property
    def values(self) -> List[float]:
        return [vector.value for vector in self.vectors]

    @property
    def times(self) -> List[float]:
        return [vector.time for vector in self.vectors]

    def show(self) -> None:
        plt.plot(self.times, self.values)
        plt.show()
