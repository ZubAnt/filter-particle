from trajectory import Trajectory
from coord import Coord
import matplotlib.pyplot as p

x, y = Trajectory(point=Coord(1, 1), k=1, step=1, size=100).generate_linear_trajectory()

p.plot(x, y)
p.show()

