"""
Checkpoint 4 Test 
"""
import numpy as np

from CP4 import Traffic
from CP4Graph import Density_graph

class CP4Test(object):

    def main():
        time_step = int(input("Number of time steps (iterations): "))
        n = int(input("N = "))
        density = float(input("Density of cars:"))

        # Apply rules and plot grid of cars
        jam = Traffic(n,time_step, density)
        jam.apply_rules(n, time_step, density)
        jam.plot_jam()

        # plot speed
        jam.plot_speed(n,time_step)
        # calculate steady state speed
        print("Steady speed = " +str(jam.steadyspeed()))
    
        # plot steady state speed against range of
        dens = Density_graph(n,time_step)
        dens.plot_stuff()

    main()
