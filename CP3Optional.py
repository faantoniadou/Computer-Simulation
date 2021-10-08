import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot(object):
    
    def __init__(self, size):
        # A grid of z-values
        X = np.linspace(-1.5,1.5,size)
        Y = np.linspace(-1.5,1.5,size)

        XX, YY = np.meshgrid(X,Y)
        self.Z = XX + 1j*YY
        
        # create grid of zeros to overwrite
        self.grid = np.zeros((size,size))

    def iterate(self, max_iter, C):
        # do iteration for given conditions 

        for i in range(0, len(self.Z)):             # iterate over grid of c-values
            for j in range(0, len(self.Z[i])):
                n = 0                                   # initialise n
                while n < max_iter and abs(self.Z[i][j]) < 2 :     # maintain number of max iterations and convergence of Z
                    n += 1
                    self.Z[i][j] = self.Z[i][j]**2 +C           
                self.grid[i][j] = n                     # insert values of n in grid
        
    def plot_mandel(self):
        # plot the grid of values of n 
        
        plt.imshow(self.grid, extent=(-2.025, 0.6, -1.125,1.125), cmap = 'CMRmap')   # set axes limits
        plt.xlabel('Re')                 # set axes titles
        plt.ylabel('Im')
        plt.colorbar()
        plt.show()


