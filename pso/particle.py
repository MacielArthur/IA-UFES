import numpy as np

class Particle():
    def __init__(self, dimension, sup_limit, inf_limit):
        self.position = np.random.uniform(inf_limit, sup_limit, dimension)
        self.speed = np.random.uniform(inf_limit, sup_limit, dimension)
        self.pbest= 0
        self.gbest = 0
        print(self.position, self.speed)

a = Particle(2, 1, 10)