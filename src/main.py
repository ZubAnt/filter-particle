from src.factories.trajectories.linear.linear_trajectory_1d_factory import LinearTrajectory1DFactory
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D

init_state = StateVectorLinear1D(time=1.0, value=1.0)
trajectory = LinearTrajectory1DFactory(state=init_state, size=100, k=1, dt=0.5).create()
trajectory.show()

# import matplotlib.pyplot as plt
# plt.plot(trajectory.times, trajectory.values)

