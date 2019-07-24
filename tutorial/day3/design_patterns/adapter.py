#
#
# Purpose: Develop classes that does not depend on each other via interfaces
# Output: Computes radius of gyration and center of mass
#
#

import numpy as np
import MDAnalysis
import mdtraj as md
from abc import ABC, abstractmethod

# Interface class that acts as a shell of methods
class TrajectoryAdapter(ABC):
    @abstractmethod
    def radius_of_gyration(self):
        pass

    @abstractmethod
    def center_of_mass(self):
        pass

# Uses the mdtraj functions and applies decorator @property
class MDTrajAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.trajectory = md.load(filename)
        print('Using MDTraj.')

    @property
    def radius_of_gyration(self):
        return 10*md.compute_rg(self.trajectory)

    @property
    def center_of_mass(self):
        return 10*md.compute_center_of_mass(self.trajectory)

class MDAnalysisAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.trajectory = MDAnalysis.Universe(filename)
#        self.trajectory = self.universe.trajectory[0]
        print('Using MDAnalysis.')

    @property
    def radius_of_gyration(self):
        rg_by_frame = np.empty(len(self.trajectory.trajectory))
        for ts in self.trajectory.trajectory:
            rg_by_frame[ts.frame] = self.trajectory.atoms.radius_of_gyration()
        return rg_by_frame
#        return self.trajectory.radius_of_gyration()

    @property
    def center_of_mass(self):
#        return self.trajectory[ ].center_of_mass(compounds='segments')
        rg_by_frame = np.ndarray(shape=(len(self.trajectory.trajectory), 3))
        for ts in self.trajectory.trajectory:
            rg_by_frame[ts.frame] = self.trajectory.atoms.center_of_mass(compound='segments')
        return rg_by_frame
    
#mdt = MDTrajAdapter('./protein.pdb')
#print(mdt.radius_of_gyration)
#print(mdt.center_of_mass)

mda = MDAnalysisAdapter('./protein.pdb')
print(mda.radius_of_gyration)
print(mda.center_of_mass)
