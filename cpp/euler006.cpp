#include <iostream>
#include <cmath>

using namespace std;


int main() {
    // Asked chatGPT if there was a simplified mathematical formula for this problem. There is.
    int n = 100;
    long long sumOfSquares = ((n * (n + 1) * (2 * n + 1)) / 6);
    long long squareOfSums = pow((n * (n + 1) / 2), 2);

    cout << squareOfSums - sumOfSquares << endl;

    return(0);
}


