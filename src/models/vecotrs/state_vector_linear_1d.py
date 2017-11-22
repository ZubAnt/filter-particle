from src.models.vecotrs.base_state_vector import BaseStateVector


class StateVectorLinear1D(BaseStateVector):

    def __init__(self, value: float, time: float) -> None:
        self._val = value
        self._t = time

    @property
    def value(self) -> float:
        return self._val

    @property
    def time(self) -> float:
        return self._t
