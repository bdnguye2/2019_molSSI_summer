#!/bin/bash

g++ --std=c++11 -fPIC --shared -Wall temperature.cpp export.cpp \
    -I /usr/local/include/python3.5 \
    -I /home/bdnguye2/.local/include/python3.5m \
    -I /usr/include/python3.5m \
    -I ~/eigen3 \
    -o sss_cpp.so
