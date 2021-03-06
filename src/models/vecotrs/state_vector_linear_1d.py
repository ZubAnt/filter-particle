from src.models.vecotrs.base_state_vector import BaseStateVector


class StateVectorLinear1D(BaseStateVector):

    def __init__(self, time: float, value: float) -> None:
        self._val = value
        self._t = time

    def __str__(self):
        return f"{{value: {self.value}, time: {self.time}}}"

    def __repr__(self):
        return f"{{value: {self.value}, time: {self.time}}}"

    @property
    def value(self) -> float:
        return self._val

    @property
    def time(self) -> float:
        return self._t

    @value.setter
    def value(self, value):
        self._value = value
