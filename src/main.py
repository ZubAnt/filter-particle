from src.factories.trajectories.linear.linear_trajectory_1d_factory import LinearTrajectory1DFactory
from src.filters.filter_particle import FilterParticle, State
from src.measurements.measure_factory import MeasureLinear1DFactory
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D

DT = 0.5    # Шаг времени

init_state = StateVectorLinear1D(time=1.0, value=1.0)
trajectory = LinearTrajectory1DFactory(state=init_state, size=100, k=1, dt=DT).create()

# trajectory.show()

measurements = MeasureLinear1DFactory(trajectory, sigma_v=1).create()
measurements.show()
filter_object = FilterParticle(measurements=measurements, part_number=1000, sigma_v=1, sigma_k=0.1,
                               t0=init_state.time, dt=DT)
filtering_trajectory = filter_object.filter()
print(trajectory.vectors)
print(measurements.vectors)
print(filtering_trajectory.vectors)

filtering_trajectory.show()


# vectors = filter_object._create_random_vectors(State(measurements.first.value, 0))



