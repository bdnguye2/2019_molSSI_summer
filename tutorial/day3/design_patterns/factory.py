#
#
# Purpose: Factory design pattern that keeps the code consistent
#          without needing to redesigning to adapt certain variables
# Output: Uses Lennard Jones and Buckingham potentials interchangeable
#
#

import numpy as np

# Defines the Lennard Jones Potential
class LJ:
    def __init__(self, epsilon, sigma):
        self.sigma = sigma
        self.epsilon = epsilon

    def get_energy(self, r):
        return 4*self.epsilon*((self.sigma/r)**12-(self.sigma/r))

# Defines the Buckingham Potential
class Buckingham:
    def __init__(self,rho,A,C):
        self.rho = rho
        self.A = A
        self.C = C

    def get_energy(self,r):
        return self.A*np.exp(-r/self.rho) - self.C/r**6

# Function that utilizes the classes as variables
def potential_factory(potential_type, **kwargs):
    if potential_type == 'LJ':
        return LJ(**kwargs)
    elif potential_type == 'Buckingham':
        return Buckingham(**kwargs)
    else:
        raise TypeError('Potential type not recognized.')

# Computation using the LJ and Buckingham Potentials
lj_potential = potential_factory('LJ', epsilon=1, sigma=1)
print(lj_potential.get_energy(r = 10.0))

buck_potential = potential_factory('Buckingham', A=1.0, rho=10.0, C=10)
print(buck_potential.get_energy(r=10.0))
