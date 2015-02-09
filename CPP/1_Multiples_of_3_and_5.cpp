#include <iostream>

int main()
{
    std::cout << "Hello World!\n";
    int total = 0;
    for (int i = 0; i < 1000; i++) {
      int num = i;
      if (num % 3 == 0 || num % 5 == 0) {
        total += num;
      }
    }
    std::cout << "Total: " << total << std::endl;
    return 0;
}
