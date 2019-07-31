#!/bin/bash

g++ -fPIC --shared -Wall test.cpp export.cpp \
    -I /home/bdnguye2/anaconda3/include \
    -I /home/bdnguye2/anaconda3/include/python3.7m \
    -I /home/bdnguye2/eigen-eigen-323c052e1731 \
    -I /home/bdnguye2/anaconda3/lib -lpython3.5m \
    -o sss_cpp.so
