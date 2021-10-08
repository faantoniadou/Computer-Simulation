from CP1 import Polynomial

def main():
    pol1 = Polynomial([2,0,4,-1,0,6])
    pol2 = Polynomial([-1,-3,0,4.5])
    pol2.polyadd(pol2)

    print(str(pol2))

    pol1.antiderivative()
    print(" The antiderivative of the polynomial is "  + str(pol1.antiderivative))

    pol1.derivative()
    print(" The derivative of the polynomial is "  + str(pol1.derivative))
main()
    
