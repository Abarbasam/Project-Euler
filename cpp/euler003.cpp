#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int num) {
    // Low prime check. If number does not fall within the set
    // defined by f(k) = 6k += 1, kEN, it is not prime
    if (num <= 1) return false;
    if (num == 2 || num == 3) return true;
    if (num % 6 != 1 && num % 6 != 5) return false;

    for (int i = 5; i < sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}


int main() {
    long num = 600851475143;
    int largest_factor = -1;

    // The problem is only concerned about finding the largest prime factor.
    // Start searching for prime factors from sqrt(num) going down. 
    for (int i = floor(sqrt(num)); i >= 2; i--) {
        if (num % i == 0) {
            if (is_prime(i)) {
                largest_factor = i;
                break;
            }
        }
    }
    
    cout << largest_factor << endl;

    return 0;
}

