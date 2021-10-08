"""
Radioactive Decay class
"""
import numpy as np
import random as random
import math 
 

class RadioDecay(object):
    
    def __init__(self, n):
        # create n x n array of ones
        self.grid = []
        for i in range(n):
            self.grid.append([1])
            for j in range(n):
                self.grid[i].append(1)

    def printGrid(self):
        #print grid of undecayed nuclei
        for i in range(0, len(self.grid)):
            s = ""
            for j in range(len(self.grid[i])):
                s += str(self.grid[i][j]) + " "
            print(s)
    
    def decay(self, timestep, dec_const):
        # choose nuclei to decay.
        
        time = 0
        p = float(dec_const * timestep) 

        print("Probability of decay: " + str(p))
        
        while np.count_nonzero(self.grid) >= 0.5*(len(self.grid)**2 + 1):     # run loop until half nuclei decay
            time += timestep
            
            for i in range (0, len(self.grid)):             # iterate through array
                for j in range(len(self.grid[i])):
                    if self.grid[i][j]== 1:                 # ensure nucleus has not already decayed
                        randomnumber = random.random()      # generate random number between 0 and 1
                        if (p > randomnumber):              # compare random number to probability of decay
                            self.grid[i][j] = 0
                            
        self.printGrid()        
        print("Simulated half life = " + str(time) + " minutes")
        print("Number of undecayed nuclei: " + str(np.count_nonzero(self.grid)))       
                 
    def print_life(self, dec_const):                        #print the actual half life using λ
        t = self.t_actual = float((math.log(2))/dec_const)
        print("Actual half life as given by the decay constant: " + str(t) + " minutes")