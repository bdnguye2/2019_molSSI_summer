#include <iostream>
#include <vector>
#include <Eigen/Dense>

double f_to_celsius(double f_temp);

double c_to_kelvin(double c_temp);

double f_to_kelvin(double f_temp);

std::vector<double> convert_vector(std::vector<double> temp_vec);

Eigen::MatrixXd convert_matrix(Eigen::MatrixXd temp_matrix);
