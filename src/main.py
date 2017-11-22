from src.factories.trajectories.linear.linear_trajectory_1d_factory import LinearTrajectory1DFactory
from src.filters.filter_particle import FilterParticle, State
from src.measurements.measure_factory import MeasureLinear1DFactory
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D
import matplotlib.pyplot as plt

DT = 20    # Шаг времени

init_state = StateVectorLinear1D(time=1.0, value=1.0)

trajectory = LinearTrajectory1DFactory(state=init_state, size=25, k=1, dt=DT).create()

measurements = MeasureLinear1DFactory(trajectory, sigma_v=20).create()

filtered_measurements = FilterParticle(measurements=measurements,
                                       part_number=10000, sigma_v=100, t0=init_state.time, dt=DT).filter()

traj_time, traj_val = trajectory.params()
meas_time, meas_val = measurements.params()
filt_time, filt_val = filtered_measurements.params()

plt.plot(traj_time, traj_val, 'r')
plt.show()

plt.plot(meas_time, meas_val, 'b')
plt.show()

plt.plot(filt_time, filt_val, 'g')
plt.show()

plt.plot(traj_time, traj_val, 'r')
plt.plot(meas_time, meas_val, 'b')
plt.show()

plt.plot(traj_time, traj_val, 'r')
plt.plot(filt_time, filt_val, 'g')
plt.show()


plt.plot(meas_time, meas_val, 'b')
plt.plot(filt_time, filt_val, 'g')
plt.show()


plt.plot(traj_time, traj_val, 'r')
plt.plot(meas_time, meas_val, 'b')
plt.plot(filt_time, filt_val, 'g')
plt.show()
