"""
Unit and regression test for the temperature_cpp package.
"""

# Import package, test suite, and other packages as needed
import temperature_cpp
import pytest
import sys

def test_temperature_cpp_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "temperature_cpp" in sys.modules
