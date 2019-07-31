#include "box.hpp"
#include <iostream>
#include <Eigen/Dense>
#include <vector>
#include <math.h>
// C++ box class

double Box::volume(void)
 /*Calculate the box volume

  Returns
  -------
  box volume : float
      Computed box volume
  */
{
  double tmp = 1.0;
  int ncols = box_dims.cols();
  for(int i = 0; i < ncols; i++)
    tmp *= box_dims(i);
  return tmp;
}

Eigen::MatrixXd Box::coord_wrap(void)
/*Wraps coordinates within the box dimension

 Returns
 -------
 wrapped : matrix
     Arrays of the wrapped atomic coordinates.
 */    
{
  int nrows = coordinates.rows();
  int ncols = coordinates.cols();
  std::cout << nrows << std::endl;
  Eigen::MatrixXd wrapped(nrows, ncols);
  for(int i = 0; i < nrows; i++)
    {
	for(int j = 0; j < ncols; j++)
	  wrapped(i,j) = coordinates(i,j) - box_dims(j) * int (coordinates(i,j) / box_dims(j));
    }
  return wrapped;
}

Eigen::VectorXd Box::minimum_image_dist(int i_particle)
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

  Eigen::MatrixXd coord_dist(nrows - 1, ncols);
  for(int i = 0; i < i_particle; i++)
    {
	for(int j = 0; j < ncols; j++)
	  coord_dist(i, j) = coordinates(i_particle, j) - coordinates(i, j);
    }
  for(int i = i_particle; i < nrows; i++)
    {
	for(int j = 0; j < ncols; j++)
	  coord_dist(i,j) = coordinates(i_particle, j) - coordinates(i + 1,j);
    }
  for(int i = 0; i < nrows - 1 ; i++)
    {
	for(int j = 0; j < ncols; j++)
	  coord_dist(i,j) = coord_dist(i,j) - box_dims(j) * int (coord_dist(i,j) / box_dims(j));
    }

  Eigen::VectorXd min_dist(nrows - 1);
  for(int i = 0; i < nrows - 1; i++)
    {
	double tmp = 0;
	for(int j = 0; j < ncols; j++)
	  tmp += coord_dist(i,j);
	min_dist(i) = std::sqrt(tmp);
    }
  return min_dist;
}
