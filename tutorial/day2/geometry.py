"""
geometry analysis functions
"""

import os
import numpy as np

def calculate_distance(rA, rB):
    """Calculate the distance between points A and B. Assumes rA and rB are numpy arrays."""
    dist_vec = (rA-rB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_distance_list(rA, rB):
    """Calculate the distance between points A and B. Assums rA and rB are lists."""
    squared_sum = 0
    for dim in range(len(rA)):
        squared_sum += (rA[dim] - rB[dim])**2
    
    distance = np.sqrt(squared_sum)
    return distance


def build_bond_list(coordinates, max_bond=2.93, min_bond=0):
    """ Build list of bonds from atomic coordinates based on distance (au).

    Parameters
    ----------
    coordinates : np.array
        An array of atomic coordinates.
    max_bond : float, optional
        The maximum distance between atoms to be considered a bond. Default 
        is 2.93 Bohr
    min_bond : float, optional
        The minimum distance between atoms to be considered a bond.

    Returns
    -------
    bonds : doct
        A dictionary of bonds with atom pair tuples as keys, and calculate bond
        lengths as value
    """
    num_atoms = len(coordinates)
    
    bonds = {}
    
    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance 
    
    return bonds
