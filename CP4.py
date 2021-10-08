"""
Checkpoint 4
"""

import numpy as np
import matplotlib.pyplot as plt

class Traffic(object):

    def __init__(self, N, timestep, density):
        # create a road with cars
        self.no_of_cars = int(density * N) 

        A = np.zeros(N)
        A[:self.no_of_cars] = 1
        np.random.shuffle(A)
        
        B = np.zeros((timestep, N))
        self.new = np.row_stack((A, B))
       
        self.avg_speed = [0]         # empty list for speeds
        
    def apply_rules(self, N, timestep, density):
        # method to apply rules and calculate avg speed for each step
        L = len(list(zip(*self.new)))
        
        time = 0
        self.time_step = [time]             # empty list for time
        
        
        for i in range(0,timestep):
            self.moves = []
            step = 0
             
            for j in range(0,L):            # apply rules to cells       
                if self.new[i][j] == 1:
                    if self.new[i][(j+1)%(L)] == 1:
                        self.new[i+1][j] = 1
                    elif self.new[i][(j+1)%(L)] == 0:
                        self.new[i+1][j] = 0

                elif self.new[i][j] == 0:
                    if self.new[i][(j-1)%(L)] == 1:
                            step +=1                    # make a move
                            self.new[i+1][j] = 1
                    else:
                        self.new[i+1][j] = 0
            time +=1

            # append parameters
            self.time_step.append(time)
            self.moves.append(step)
            self.average_speed(N, density)
            
        self.jam = self.new                 # grid of cars

    def average_speed(self, N, density):
        # method to calculate average speed in each step
        speed = 0 
        
        for i in range(0,len(self.moves)):   
            if self.no_of_cars == 0:
                speed = 0
                continue
            
            speed = self.moves[i]/self.no_of_cars#(density * N)
            self.avg_speed.append(speed)

    def steadyspeed(self):
        # method to calculate steady state speed
        return self.avg_speed[-1]

    def plot_jam(self):
        # plot the movement of cars
        plt.imshow(self.jam, 'binary')
        plt.xlabel('Traffic')
        plt.ylabel('Timestep')
        plt.show()
        
    def plot_speed(self, N, timestep):
        # plot average speed against time
        plt.plot(self.time_step,self.avg_speed)
        plt.xlim(0)
        plt.ylim(0)
        plt.ylabel("Average speed")
        plt.xlabel("Time/s")
        plt.show()

