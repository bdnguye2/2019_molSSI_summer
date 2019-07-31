#!/bin/bash

g++ --std=c++11 -fPIC --shared -Wall temperature.cpp export.cpp \
    `python3 -m pybind11 --includes`\
    -I ~/eigen3 \
    -o sss_cpp.so
