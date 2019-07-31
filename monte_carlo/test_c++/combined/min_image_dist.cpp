#include <iostream>
#include <Eigen/Dense>
#include <vector>
#include <math.h>

Eigen::VectorXd minimum_image_dist(index_particle, coordinates)
/*Parameters
 ----------
 i_particle : array
     xyz coordinate of the i-th particle.

 Returns
 -------
 min_dist : array
     Array of the distances between each i-th particle and remaining
     particles
*/
{
  int nrows = coordinates.rows();
  int ncols = coordinates.cols();

  Eigen::MatrixXd coord_dist(nrows, ncols);
  Eigen::VectorXd min_dist(nrows);
  for(int i = 0; i < nrows; i++)
    {
      for(int j = 0; j < index_particle; j++)
	coord_dist(i,j) = coordinates(index_particle, j) - coordinates(i,j);
    } 

  return coord_dist;
}
