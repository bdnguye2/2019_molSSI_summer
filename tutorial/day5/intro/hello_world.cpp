// iostream is like a module to start C++ program
#include <iostream>

// This is a one line comment.

/* Multiple lines commenting
   feature
*/


// defines a return type that need to be declared first
int main(void)
{
  std::cout << "Hello, world!" << std::endl;

  int a = 10;
  // A = 10 Undeclared variables yield errors
  a = 2.95;
  // C++ is highly case sensitive (a = "Hello";)
  std::cout << "a is " << a << std::endl;

  const double d = 10.0;
  /* Since 'const double d = 10.0' declared to be a constant number 10
  (d = 1.0; this will yield an error: assignment)
  */
  
  return 0;
}
