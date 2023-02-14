#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int num) {
    if (num <= 1) return false;

    for (int i = 2; i < sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}


int main() {
    long num = 600851475143;
    int largest_factor = 0;

    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            if (is_prime(i)) largest_factor = i;
            if (is_prime(num/i)) largest_factor = num/i;
        }
    }
    
    cout << largest_factor << endl;

    return 0;
}

