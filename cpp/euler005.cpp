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

long gcd(long a, int b) {
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
    
    // Find compounding least common multiple from 20 to 2. 
    for (int i = LCM - 1; i > 1; i--) {
        LCM = (LCM * i) / gcd(LCM, i); 
    }
    
    cout << LCM << endl;

    /* INFERIOR METHOD
    long LCM = 0;
    int increment = 20;
    bool LCM_found = false;

    while ( !LCM_found ) {
        LCM += increment;

        for (int i = increment - 1; i > 1; i--) {
            if ( LCM % i != 0 ) break;
            if ( i == 2 ) LCM_found = true; 
        }
    }
    */

    return(0);
}


