"""
Checkpoint 3: Mandelbrot set
============================

Compute the Mandelbrot set and plot it

"""
import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot(object):
    
    def __init__(self, size):
        # A grid of c-values
        X = np.linspace(-2.025,0.6,size)
        Y = np.linspace(-1.125,1.125,size)

        XX, YY = np.meshgrid(X,Y)
        self.C = XX + 1j*YY
        
        # create grid of zeros to overwrite
        self.grid = np.zeros((size,size))

    def iterate(self, max_iter):
        # do iteration for given conditions 
        
        for i in range(0, len(self.C)):             # iterate over grid of c-values
            for j in range(0, len(self.C[i])):
                Z = 0.0
                n = 0                                   # initialise n
                while n < max_iter and abs(Z) < 2 :     # maintain number of max iterations and convergence of Z
                    n += 1
                    Z = Z**2 +self.C[i][j]              
                self.grid[i][j] = n                     # insert values of n in grid
        
    def plot_mandel(self):
        # plot the grid of values of n 
        
        plt.imshow(self.grid, extent=(-2.025, 0.6, -1.125,1.125), cmap = 'CMRmap')   # set axes limits
        plt.xlabel('Re(C)')                 # set axes titles
        plt.ylabel('Im(C)')
        plt.colorbar()
        plt.show()


