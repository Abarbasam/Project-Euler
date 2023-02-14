/*
multiples = [] # Will contain all multiples of 3 and 5

numberCap = 1000 # The highest number that the program will check for multiples

for i in range(1, numberCap):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

print sum(multiples)
*/

#include <iostream>

int main() {
    int sum = 0;

    for (int i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }

    std::cout << sum << std::endl;

    return 0;
}
