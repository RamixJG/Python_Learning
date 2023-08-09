import math
import random
from random import random as rand


random.seed(42)
centroid = (0.5, 0.5)
points = [(rand(), rand()) for i in range(10)]

closest = [1, math.dist(centroid,points[0])]

for idx, point in enumerate(points):
    if math.dist(centroid,point) < closest[1]:
        closest = [idx, math.dist(centroid,point)]

print(tuple(closest))