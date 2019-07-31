#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include "box.hpp"
#include "potentials.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
  m.doc() = "This is example c++ module called from python";
  m.def("LJ", LJ, "Pairwise potential and correction energy by Lennard-Jones potential.");
  m.def("cutoff_correction", cutoff_correction, "The function corrects interaction energy from energy cutoff.");

  pybind11::class_<Box>(m, "Box")
    .def(pybind11::init<>())
    .def_readwrite("box_dims", &Box::box_dims, "box dimensions")
    .def_readwrite("coordinates", &Box::coordinates, "particle coordinates")
    .def("volume", &Box::volume)
    .def("coord_wrap", &Box::coord_wrap);
    //    .def("minimum_image_dist", &Box::minimum_image_dist);
}
