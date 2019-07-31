#!/bin/bash 

c++ -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` example.cpp -o example
