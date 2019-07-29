#include <iostream>
#include <vector>
#include <Eigen/Dense>

double f_to_celsius(double f_temp)
{
    return (f_temp - 32.0)/1.8;
}


double c_to_kelvin(double c_temp)
{
    return c_temp + 273.15;
}

double f_to_kelvin(double f_temp)
{
    double c_temp = f_to_celsius(f_temp);
    return c_to_kelvin(c_temp);
}

std::vector<double> convert_vector(std::vector<double> temp_vec)
{
    std::vector<double> c_temp_vec;
    for(auto it : temp_vec)
        c_temp_vec.push_back(f_to_celsius(it));

    return c_temp_vec;
}


Eigen::MatrixXd convert_matrix(Eigen::MatrixXd temp_matrix)
{
    int nrow = temp_matrix.rows();
    int ncol = temp_matrix.cols();

    Eigen::MatrixXd c_temp_matrix(nrow, ncol);

    for(int i = 0; i < nrow; i++)
    {
        for(int j = 0; j < ncol; j++)
        {
            c_temp_matrix(i, j) = f_to_celsius(temp_matrix(i, j));
        }
    }

    return c_temp_matrix;
}
