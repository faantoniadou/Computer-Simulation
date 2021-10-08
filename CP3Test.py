"""
Checkpoint 3: Mandelbrot set test 
============================

Simple test to compute the Mandelbrot set and plot it

"""

from CP3 import Mandelbrot

class CP3Test(object):

    def main():
        
        mandel= Mandelbrot(255)    # set size of array
        mandel.iterate(100)        # set max iterations 
        mandel.plot_mandel()        # plot grid of number of iterations 

    main()