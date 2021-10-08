'''
Polynomial Class
'''

from operator import add

class Polynomial(object):

    coeffs = []

    def __init__(self, coeffs):
        """
        Constructor to form a polynomial
        """
        self.coeffs = coeffs

    def order(self):
        """
        Method to return order of polynomial
        """
        return len(self.coeffs) - 1
    
    def polyadd(self, other):
        """
        Method to add two polynomials and return as new polynomial
        """
        # conditions for lists of different lengths
        
        if len(self.coeffs) > len(other.coeffs):    
            for i in range(len(other.coeffs), len(self.coeffs)):
                other.coeffs.insert(i, 0)
                
        elif len(self.coeffs) < len(other.coeffs):
            for i in range(len(self.coeffs), len(other.coeffs)):
                self.coeffs.insert(i, 0)
       
        new_coeffs = list(map(add, self.coeffs, other.coeffs))
        
        return Polynomial(new_coeffs)

    def derivative(self):
        """
        Method to calculate the derivative
        """
        derivative_coeffs = []                  #empty list for new coefficients
    
        for i in range(1,len(self.coeffs) - 1 ):
            # loop to append coefficients of derivative
            derivative = self.coeffs[i] * i
            derivative_coeffs.append(derivative)

        return Polynomial(derivative_coeffs)

    def antiderivative(self):
        """
        Method to calculate the antiderivative
        """
        antiderivative_coeffs = []                  #empty list for new coefficients
        
        for k in range(0, len(self.coeffs)):
            # loop to append coefficients of antiderivative
            antiderivative = float(self.coeffs[k]/(k + 1))
            antiderivative_coeffs.append(antiderivative)
            
        antiderivative_coeffs.insert(0,2)                   #insert constant of integration
        
        return Polynomial(antiderivative_coeffs)

    def printPol(self):
        """
        Method to print a string representation of the polynomial 
        """
        printed = str()
        
        for m in range(1, len(self.coeffs) ):
            
            if self.coeffs[m] != 0:             #omit terms with coefficient 0

                #coefficient sign conditions
                if self.coeffs[m] > 0:
                    printed += (" + ")
                elif self.coeffs[m] < 0:
                    printed += (" - ")

                #conditions to omit printing 1x
                if self.coeffs[m] != 1 and self.coeffs[m] != -1:
                    printed += (str(abs(self.coeffs[m])))       #take absolute value to avoid double signs

                #conditions to omit printing x^1
                if m == 1:
                    printed += ("x")
                elif m != 1:
                    printed += ("x^" + str(m))
                
        return (str(self.coeffs[0]) + str(printed))