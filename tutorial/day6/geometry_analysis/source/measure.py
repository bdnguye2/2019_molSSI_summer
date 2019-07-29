"""
measure.py
A python package for the MolSSI Software Summer School.
Contains a measure class to print out bond distances and angles.
Module example.
"""

import numpy as np

def calculate_distance(rA, rB):
    """Calculate the distance between points A and B.
    
    Parameters
    ----------
    rA : numpy array
        The x, y, z coordinates of point A
    rB : numpy array
        The x, y, z coordinates of point B
    
    Returns
    -------
    distance : float
        The distance between points A and B.
    
    Examples: Runs pytest within the measure module
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1,r2)
    0.1
    """
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    return distance


def calculate_angle(rA, rB, rC, degrees=False):
    """Calculate angle between points A, B, and C
    
    Parameters
    ----------
    rA : numpy array
        The x, y, z coordinates of point A
    rB : numpy array
        The x, y, z coordinates of point B
    degrees : bool, optional
        Return the calculated angle in degrees.
    
    Returns
    -------
    angle : float
        The distance between points A and B.
    """
    AB = rB - rA
    BC = rB - rC

    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
