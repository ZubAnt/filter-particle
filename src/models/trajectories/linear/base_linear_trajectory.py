from typing import List, TypeVar, Generic, Optional

S = TypeVar("State")


class BaseLinearTrajectory(Generic[S]):

    def __init__(self):
        self._vectors: List[S] = []

    @property
    def vectors(self) -> List[S]:
        return self._vectors

    @property
    def size(self) -> int:
        return len(self.vectors)

    @property
    def last(self) -> Optional[S]:
        if not self.vectors:
            return None
        return self.vectors[self.size - 1]

    @property
    def first(self) -> Optional[S]:
        if not self.vectors:
            return None
        return self.vectors[0]

    def append(self, state: S) -> None:
        self._vectors.append(state)
