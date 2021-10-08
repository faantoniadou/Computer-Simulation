
import math
from CP2 import RadioDecay

class CP2Test(object):
    
    def main():
        n = int((input( "Length of the array: " )))
        delta_t = float(input("Timestep: "))

        '''print actual half life'''
        decayconstant = float(input( "Decay constant, λ = " ))
        print("Actual half life = " + str((math.log(2))/decayconstant) + "minutes")

        '''print the grid'''
        print("Initial array of undecayed nuclei: ")

        r = RadioDecay(n)
        r.printGrid()
        r.decay(delta_t,decayconstant)
        r.print_life(decayconstant)

    main()