#include <iostream>
// Converts fahrenheit to celcius and to kelvin

double f_to_celsius(double f_temp)
// double is a data type for double precision
{
  return (f_temp - 32.0)/1.8;
}

double cel_to_kelvin(double c_temp)
{
  return c_temp + 273.15;
}

int main(void)
{
  double f = 100.0;
  double c = f_to_celsius(f);
  double k = cel_to_kelvin(c);
  std::cout << "F = " << f << std::endl
	    << "C = " << c << std::endl
	    << "K = " << k << std::endl;
  
  return 0;
}
