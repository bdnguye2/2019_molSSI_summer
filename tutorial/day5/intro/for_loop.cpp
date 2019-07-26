#include <iostream>

// Traditional standard for loop
void count(int max)
{
  // i++ denotes i += 1
  for(int i = 0; i < max; i++)
    std::cout << "i is " << i << std::endl;
}

int main(void)
{
  count(100);
}
