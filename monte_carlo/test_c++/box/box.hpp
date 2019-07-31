
#pragma once

#include <iostream>
#include <Eigen/Dense>
#include <vector>
#include <math.h>

class Box
{
  public:
   Eigen::VectorXd box_dims;
   Eigen::MatrixXd coordinates;

  double volume(void);

  Eigen::MatrixXd coord_wrap(void);

  Eigen::VectorXd minimum_image_dist(int i_particle);

};
