#include <iostream>
#include <numeric>
// Two methods --------------
// One: With numbers from 20 to 1, find the LCM of 20 and it's next element 19
//      Find he LCM of this result and 18. Find the LCM of that result and 17. And so on.
//
//
// Two:
//     Increment number by 20. Try modding by every number from 2-20 and break early if result is NOT 0.
//
//
// METHOD ONE:
//


using namespace std;

long gcd(long a, long b) {
    int r = 0;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    long LCM = 20;
    
    for (long i = LCM - 1; i > 1; i--) {
        LCM = (LCM * i) / gcd(LCM, i); 
    }

    cout << LCM << endl;
    return(0);
}


