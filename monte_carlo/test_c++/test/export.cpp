#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include "test.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
  m.doc() = "This is example c++ module called from python";
  m.def("test", coord_wrap);
}
