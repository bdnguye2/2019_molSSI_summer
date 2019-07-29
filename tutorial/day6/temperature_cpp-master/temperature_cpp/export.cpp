#include "temperature.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>


PYBIND11_MODULE(temperature_cpp, m)
{
    m.doc() = "Functions for converting temperature implemented in C++";
    
    m.def("f_to_celsius", f_to_celsius, "Convert Fahrenheit to Celsius");
    m.def("c_to_kelvin", c_to_kelvin, "Convert Celsius to Kelvin");
    m.def("f_to_kelvin", f_to_kelvin, "Convert Fahrenheit to Kelvin");
    m.def("convert_vector", convert_vector, "Convert a list of Fahrenheit to Celsius");
    m.def("convert_matrix", convert_matrix, "Convert a matrix of Fahrenheit to Celsius");
}
