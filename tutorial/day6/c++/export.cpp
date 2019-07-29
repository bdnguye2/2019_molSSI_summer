#include <pybind11/pybind11.h>
#include "temperature.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
  m.doc() = "This is example c++ module called from python";
}
