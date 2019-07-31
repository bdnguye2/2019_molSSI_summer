#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include "temperature.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
  m.doc() = "This is example c++ module called from python";
  m.def("f_to_celsius", f_to_celsius, "Convert fahrenheit to celsius");
  m.def("c_to_k", c_to_k, "Convert celcius to kelvin");
  m.def("check_temperature", check_temperature, "Check the temperature");
  m.def("count", count, "Integrator");
  m.def("f_to_c_vector", f_to_c_vector, "Convert a vector of F to C");
  m.def("f_to_c_matrix", f_to_c_matrix, "Convert a matrix of F to C");
}
