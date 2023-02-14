#include <iostream>

int main() {
    int buf1 = 1;
    int buf2 = 1;
    int next_fib_num = buf1 + buf2;
    int sum = 0;

    // Summing all even fibonacci numbers less than 4 million.
    while (next_fib_num < 4000000) {
        if (next_fib_num % 2 == 0) {
            sum += next_fib_num;
        }
        // Increment the correct buffer to get the next fibonacci number
        if (buf1 < buf2) { buf1 = next_fib_num; }
        else { buf2 = next_fib_num; }

        next_fib_num = buf1 + buf2;
    }

    // Print result
    std::cout << sum << std::endl;

    return 0;
}
