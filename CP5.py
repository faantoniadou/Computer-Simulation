import numpy as np
import math
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.preprocessing import normalize
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]

class Body(object):

    G = 6.6742E-11          # m^3 / (kg * s^2)

    def __init__(self, mass, location, velocity):
        
        self.mass = mass
        self.location = location
        self.velocity = velocity

    def updated_acceleration(self, bodies, i):

        current_body = bodies[i]
        self.acceleration = np.array([0,0])

        for k in range(len(bodies)):
            while k != i:
                other_body = bodies[k]
                r = current_body.location - other_body.location
                acceleration += - G * (other_body.mass / (np.abs(r)^2)) * np.linalg.norm(r)
       
        print(str(acceleration))
        return acceleration
    
    def update_velocity(self, bodies, i):
        
        current_body = bodies[i]
        current_body.velocity = current_body.initial_velocity

        for i in range(len(bodies)):
            current_body.velocity += updated_acceleration * self.time_step
            print(str(current_body.velocity))

    def update_position(self, bodies):
        for current_body in bodies:
            current_body.location += current_body.velocity * self. time_step
        return current_body.location
'''
class Simulation(object):
    
    location_map = []

    def __init__(self):
        G = 6.6742E-11
        self.period = (2*math.pi) / math.sqrt(G * self.mass)
        self.location_map = location_map

        # set simulation parameters
        self.no_of_steps = 1000
        self.time_step = self.period / self.no_of_steps

        self.time_list = np.arange(0, self.period,self.time_step)
    
    def calculate_acceleration(self):

        acceleration = np.array([0,0])

        for i in range(0,len(time_list)):
            acceleration = Body.updated_acceleration
            return acceleration

    def calculate_velocity(self,n):

        velocity = [(0,0)]

        for i in range(0,len(time_list)):
            acceleration = Body.updated_acceleration
            velocity += velocity + acceleration * self.time_step
        return velocity
    
    def calculate_position(self, n):
        
        position = Body.update_position
        velocity = calculate_velocity

        for i in range(0,len(time_list)):
            position += position + velocity * self.time_step
            self.location_map.append(position)
        return position

    def eulercromer(self):
        bodies = self.bodies[n]
        body_location = []

        for i in range(0, self.no_of_steps):
            bodies.calculate_acceleration
            bodies.calculate_velocity
            bodies.calculate_position
            #update Mars
            #update acceleration
            #update velocity
           

            #update Phobos
            #update acceleration
            #update velocity
        return bodies.calculate_position
'''
def main():
    G = 6.6742E-11          # m^3 / (kg * s^2)
    
    # Mars Parameters:
    mars = {"location":np.array([0,0]), "mass":6.4185E23, "initial_velocity":np.array([0,0])}

    # Phobos Parameters:
    phobos_v_initial = math.sqrt((G * mars["mass"])/9.3773E6)
    phobos = {"location":np.array([9.3773E6,0]), "mass":1.06E16, "initial_velocity":np.array([0, phobos_v_initial])}
 
    # Take into account all bodies
    bodies = [
        Body( location = mars["location"], mass = mars["mass"], velocity = mars["initial_velocity"]),
        Body( location = phobos["location"], mass = phobos["mass"], velocity = phobos["initial_velocity"]),
        ]
 
    # Check if first class works:
    acc = bodies.updated_acceleration(bodies,1)
    v = bodies.update_velocity(bodies, 1)

main()
