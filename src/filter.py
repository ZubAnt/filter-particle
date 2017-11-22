# from typing import List
# from numpy import random as r
#
# from trajectory import Trajectory
#
#
# class Filter(object):
#
#     def __init__(self, trajectory: Trajectory):
#         self._trajectory = trajectory
#         self._x, self._y = trajectory.generate_linear_trajectory()
#
#     def init_random_vector(self, size: int, dx: float, dy: float):
#         vec_x = r.uniform(low=self._x[0] - dx / 2, high=self._x[0] + dx / 2, size=size)
#         vec_y = r.uniform(low=self._y[0] - dy / 2, high=self._y[0] + dy / 2, size=size)
#
#         return vec_x, vec_y
#
#     def next(self, curr_x, curr_y):
#         new_vec_x = map(lambda x: x + self._trajectory.step, curr_x)
#         new_vec_y = []
#
#         for i in range(len(curr_x)):
#             new_y = curr_y[i] + self._trajectory.k * curr_x[i]
#             new_vec_y.append(new_y)
#
#         return new_vec_x, new_vec_y
#
#     def foo(self):
#         curr_x, curr_y = self.init_random_vector(10, 0.2, 0.2)
#         next_x, next_y = self.next(curr_x, curr_y)
#
#
#
#
#
#
#
