from CP3Optional import Mandelbrot

class CP3Test(object):

    def main():
        
        mandel= Mandelbrot(1000)    # set size of array
        mandel.iterate( 255, -0.28 - 0.64j)        # set max iterations 
        mandel.plot_mandel()        # plot grid of number of iterations 

    main()