#include <iostream>
#include <vector>
#include "hello_world.hpp"

int main(void)
{
  std::vector<double> my_vector;
  my_vector.push_back(3.1415);
  std::cout << "0th element is " << my_vector[0] << std::endl;
  std::cout << "0th element is " << my_vector.at(0) << std::endl;

  std::cout << "1st element is " << my_vector[1] << std::endl;
  std::cout << "1st element is " << my_vector.at(1) << std::endl;
  
  std::cout << "My vector has " << my_vector.size() << " elements" << std::endl;
  return 0;

//  std::cout << "Hello, world!" << std::endl;
//
//  int a = 10;
//  // A = 10 Undeclared variables yield errors
//  a = 2.95;
//  // C++ is highly case sensitive (a = "Hello";)
//  std::cout << "a is " << a << std::endl;
//
//  count(5);
//  double f = 100.0;
//  double c = f_to_celsius(f);
//  double k = cel_to_kelvin(c);
//  std::cout << "F = " << f << std::endl
//            << "C = " << c << std::endl
//            << "K = " << k << std::endl;  
//  
//  return 0;
}
