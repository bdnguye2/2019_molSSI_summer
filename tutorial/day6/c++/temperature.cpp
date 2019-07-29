#include <iostream>

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


