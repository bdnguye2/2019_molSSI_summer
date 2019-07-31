#include <iostream>
#include <Eigen/Dense>
#include <vector>

const double zero_k_in_c = 273.15;

double f_to_celsius(double f_temp)
{
    return (f_temp - 32.0)/1.8;
}


double c_to_k(double c_temp)
{
    return c_temp + 273.15;
}

double f_to_kelvin(double f_temp)
{
    double c_temp = f_to_celsius(f_temp);
    return c_to_k(c_temp);
}

// Returns false if f_temp is unphysical
bool check_temperature(double f_temp)
{
    double k = f_to_kelvin(f_temp);
    if(k <= 0.0 || k > 1.0e6)
        return false; 
    else
        return true;
}


void count(int max)
{
    for(int i = 0; i < max; i++)
        std::cout << "i is " << i << std::endl;
}

std::vector<double> f_to_c_vector(std::vector<double> f_vec)
{// convert all elements of f_vec from fahrenheit to celsius
  std::vector<double> c_vec;
  for(auto it : f_vec)
    c_vec.push_back(f_to_celsius(it));
  return c_vec;
}

Eigen::MatrixXd f_to_c_matrix(Eigen::MatrixXd f_mat)
{ // convert all elements of f_mat to celsius
  int nrows = f_mat.rows();
  int ncols = f_mat.cols();
  Eigen::MatrixXd c_mat(nrows, ncols);
  for(int i = 0; i < nrows; i++)
    {
      for(int j = 0; j < ncols; j++)
	c_mat(i,j) = f_to_celsius(f_mat(i,j));
    }
  return c_mat;
}
