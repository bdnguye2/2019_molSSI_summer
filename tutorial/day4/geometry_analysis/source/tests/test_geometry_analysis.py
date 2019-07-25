"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import source
import pytest
import sys

import numpy as np

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "source" in sys.modules

def test_calculate_distance():
    """Test the calculate_distance function"""

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])

    expected_distance = np.sqrt(2.)

    calculated_distance = source.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance
