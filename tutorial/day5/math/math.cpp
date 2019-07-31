#include <iostream>
#include <vector>
#include <Eigen/Dense>

int main(void)
{
  Eigen::MatrixXd mat(2,3);
  Eigen::VectorXd vec(3);

  mat(0,0) = 1.0;
  mat(0,1) = 2.0;
  mat(0,2) = 3.0;
  mat(1,0) = 4.0;
  mat(1,1) = 5.0;
  mat(1,2) = 6.0;

  vec(0) = vec(1) = vec(2) = 1.0;

  std::cout << "v.v = " << vec.dot(vec) << std::endl;

  Eigen::MatrixXd mat2 = mat * mat.transpose();
  
  std::cout << mat << std::endl << std::endl;
  
  std::cout << mat2 << std::endl;

  // Matrix multiplication: 2x3 * 3x1 = 2x1
  Eigen::MatrixXd vmult = mat * vec;
  std::cout << "vmult" << std::endl << vmult << std::endl;
  
  return 0;
}
