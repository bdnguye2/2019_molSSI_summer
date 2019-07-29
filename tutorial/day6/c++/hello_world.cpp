#include <iostream>
#include <vector>
#include <string>
#include "temperature.hpp"

void print_vector(std::vector<double> & vec)
// Prints out the elements of the array
{
  // First way of writing the loop
  //for(size_t i = 0; i < vec.size(); i++)
  // Will work but lead to compiler warning; should be 'size_t i' not 'int i'
  //  std::cout << "Element " << i << " is " << vec[i] << std::endl;
  
  // Range-based for loop similar to python
  for(double it : vec)
    std::cout << it << std::endl;
  vec[0] = 0.000;
}

int main(void)
{
  std::vector<double> my_vector;
  my_vector.push_back(3.1415);
  std::cout << "0th element is " << my_vector[0] << std::endl;
  std::cout << "0th element is " << my_vector.at(0) << std::endl;

  std::cout << "1st element is " << my_vector[1] << std::endl;
  //std::cout << "1st element is " << my_vector.at(1) << std::endl;
  // Line of code will compiled but the program won't run giving index error

  std::string s = "This is a string";
  std::cout << "s is " << std::endl;
  
  std::vector<double> multiples;
  for(int i = 1; i < 6; i++)
    {
      double k = 3.1415 * i;
      multiples.push_back(k);
    }
  print_vector(multiples);
  std::cout << "0th element: " << multiples[0] << std::endl;
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
