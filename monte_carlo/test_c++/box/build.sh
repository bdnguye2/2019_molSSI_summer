#!/bin/bash

g++ -fPIC --shared -Wall box.cpp export.cpp \
    -I /home/bdnguye2/anaconda3/include \
    -I /home/bdnguye2/anaconda3/include/python3.7m \
    -I /home/bdnguye2/eigen3 \
    -I /home/bdnguye2/anaconda3/lib -lpython3.5m \
    -o sss_cpp.so
