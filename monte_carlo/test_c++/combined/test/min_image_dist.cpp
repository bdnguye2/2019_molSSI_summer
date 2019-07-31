#include <iostream>
#include <Eigen/Dense>
#include <vector>
#include <math.h>

Eigen::VectorXd minimum_image_dist(int index_particle, Eigen::MatrixXd coordinates)
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
  for(int i = 0; i < nrows; i++)
    {
      for(int j = 0; j < index_particle; j++)
	coord_dist(i,j) = coordinates(index_particle, j) - coordinates(i,j);
    } 

  return coord_dist;
}

int main(void)
{
  Eigen::MatrixXd coord(3,3);
  coord(0,0) = 0.1;
  coord(0,1) = 1.2;
  coord(0,2) = 2.1;
  coord(1,0) = 0.5;
  coord(1,1) = 1.5;
  coord(1,2) = 2.1;
  coord(2,0) = 0.4;
  coord(2,1) = 0.7;
  coord(2,2) = 1.9;
  
  Eigen::VectorXd dims(3);
  dims(0) = 2;
  dims(1) = 2;
  dims(2) = 2;
  
  std::cout << coord() << std::endl;

  return 0;
}

