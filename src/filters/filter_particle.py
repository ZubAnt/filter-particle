from functools import reduce
from typing import List

import numpy as np

from src.models.trajectories.linear.linear_trajectory_1d import LinearTrajectory1D
from src.models.vecotrs.state_vector_linear_1d import StateVectorLinear1D


class State(object):

    def __init__(self, value: float, k: float):
        self._value = value
        self._k = k

    @property
    def value(self) -> float:
        return self._value

    @property
    def k(self) -> float:
        return self._k

    def __str__(self) -> str:
        return f"{{v: {self.value}, k: {self.k}}}"

    def __repr__(self) -> str:
        return f"{{v: {self.value}, k: {self.k}}}"


class FilterParticle(object):

    def __init__(self, measurements: LinearTrajectory1D, part_number: int,
                 sigma_v: float, t0: float, dt: float) -> None:
        """
        :param measurements: Отметки измерений траектории
        :param part_number: количество генерируемых случайных векторов
        :param sigma_v: СКО параметра "value"
        :param t0: начальный момент времени
        :param dt: шаг времени
        """
        self._sigmaV = sigma_v
        self._partNumber = part_number
        self._measurements = measurements
        self._t0 = t0
        self._dt = dt

    def filter(self) -> LinearTrajectory1D:

        if self._measurements.size <= 2:
            raise Exception

        print(f"filter progress 0  %")
        trajectory_accuracy = LinearTrajectory1D()

        vectors_of_measurements = self._measurements.vectors

        prev_measure = vectors_of_measurements[0]
        var = prev_measure.value
        trajectory_accuracy.append(prev_measure)
        prev_measure_state = State(value=prev_measure.value, k=0)

        curr_step_pc = 10
        for i in range(1, self._measurements.size):

            curr_pc = (i / self._measurements.size) * 100
            if curr_pc > curr_step_pc:
                print(f"filter progress {curr_step_pc} %")
                curr_step_pc += 10

            curr_measure = vectors_of_measurements[i]
            k = (curr_measure.value - prev_measure.value) / self._dt
            curr_measure_state = State(value=curr_measure.value, k=k)

            state_accuracy = self.get_accuracy_value(prev_measure_state=prev_measure_state,
                                                     curr_measure_state=curr_measure_state)
            accuracy = StateVectorLinear1D(value=state_accuracy.value + var, time=self._t0 + i * self._dt)
            trajectory_accuracy.append(accuracy)
            prev_measure_state = state_accuracy

        print(f"filter progress {100}%")
        print("Completed")

        return trajectory_accuracy

    def get_accuracy_value(self, prev_measure_state: State, curr_measure_state: State) -> State:

        random_vectors = self._create_random_vectors(state=prev_measure_state)
        ext_random_vectors = []

        for random_state in random_vectors:
            ext_random_state = self.extrapolate(random_state)
            ext_random_vectors.append(ext_random_state)

        ext_sigma_v = self._calculate_rms_of_value(measure_state=curr_measure_state, random_vectors=ext_random_vectors)
        weights = self._calc_weights_for_values(measure_state=curr_measure_state,
                                                ext_sigma_v=ext_sigma_v, ext_random_vectors=ext_random_vectors)
        normalized_weights = self._normalized_weight(weights)

        v_accuracy = reduce(lambda accumulator, i: accumulator + normalized_weights[i] * ext_random_vectors[i].value,
                            range(len(normalized_weights)), 0)

        # k_accuracy = reduce(lambda accumulator, i: accumulator + normalized_weights[i] * ext_random_vectors[i].k,
        #                     range(len(normalized_weights)), 0)

        k_accuracy = (v_accuracy - prev_measure_state.value) / self._dt
        state_accuracy = State(value=v_accuracy, k=k_accuracy)
        return state_accuracy

    def extrapolate(self, state: State) -> State:
        ext_v = state.value + state.k * self._dt
        ext_k = state.k
        return State(value=ext_v, k=ext_k)

    @staticmethod
    def _normalized_weight(weights: List[float]) -> List[float]:
        s = sum(weights)
        return [w / s for w in weights]

    # RMS == СКО
    @staticmethod
    def _calculate_rms_of_value(measure_state: State, random_vectors: List[State]) -> float:
        n = len(random_vectors)
        s = reduce(lambda accumulator, state: accumulator + (state.value - measure_state.value) ** 2, random_vectors, 0)
        return np.sqrt(s / n)

    def _calc_weights_for_values(self, measure_state: State, ext_sigma_v: float,
                                 ext_random_vectors: List[State]) -> List[float]:
        weights = []
        measure_value = measure_state.value
        for ext_state in ext_random_vectors:
            ext_value = ext_state.value
            weight = self._calc_weight(measure_value=measure_value, ext_value=ext_value, ext_sigma_v=ext_sigma_v)
            weights.append(weight)

        return weights

    @staticmethod
    def _calc_weight(measure_value: float, ext_value: float, ext_sigma_v: float) -> float:
        e = np.exp(- (ext_value - measure_value)  ** 2 / (2 * (ext_sigma_v ** 2)))
        z = np.sqrt(2 * np.pi * (ext_sigma_v ** 2))
        return e / z

    def _create_random_vectors(self, state: State) -> List[State]:
        v = state.value
        k = state.k

        vectors = []
        for i in range(self._partNumber):
            new_v = np.random.normal(loc=v, scale=self._sigmaV)
            new_k = (new_v - v) / self._dt
            vectors.append(State(value=new_v, k=new_k))

        return vectors




