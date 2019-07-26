#include <iostream>
// <iostream> is can be viewed as a module to initialize c++
/*
Converts fahrenheit to celcius and to kelvin
*/

/* Mutable global variables are not recommended; Const makes
the variable immutable
*/
const double zero_k = 273.15;

double f_to_celsius(double f_temp)
// double is a data type for double precision
{
  return (f_temp - 32.0)/1.8;
}

double cel_to_kelvin(double c_temp)
{
  return c_temp + 273.15;
}

double f_to_kelvin(double f_temp)
{
  double c_temp = f_to_celsius(f_temp);
  return cel_to_kelvin(c_temp);
}

bool check_temperature(double f_temp)
// bool is a boolean type
{
  double k = f_to_kelvin(f_temp);
  if(k <= 0.0 || k > 1.0e6)
    return false;
  /*  else if(k > 1.0e6)
   return false; these lines are commented since '||' means 'or'
   '&&' means 'and'
  */
  else
    return true;
}
/* Keep in mind declaration order does not matter but if function
being used before, must come after
*/


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
