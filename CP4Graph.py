"""
Plot a graph for a range of densities for Checkpoint 4
"""

import numpy as np
import matplotlib.pyplot as plt
from CP4 import Traffic

class Density_graph(object):

    def __init__(self, N, timestep):
        self.steady = []
        self.range_densities = np.linspace(1/N,1,N-1)

        for i in range(0,len(self.range_densities)):
            jam = Traffic(N, timestep, self.range_densities[i]) 
            jam.apply_rules(N, timestep, self.range_densities[i])
            steady_speed = jam.steadyspeed()
            self.steady.append(steady_speed)        
    
    def plot_stuff(self):
        plt.plot(self.range_densities, self.steady)
        plt.xlim(0,1)
        plt.ylim(0,1.1)
        plt.ylabel("Steady state speed")
        plt.xlabel("Density")
        plt.show()

