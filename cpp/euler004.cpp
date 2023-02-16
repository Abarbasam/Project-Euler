#include <iostream>
#include <algorithm>

using namespace std;


// Check if an integer number is palindromic
bool isPalindrome(int num) {
    string number = to_string(num);
    
    // cop and reverse the number. Check if the original and reverse equal
    string numberReverse = number;
    reverse(numberReverse.begin(), numberReverse.end());

    if (number == numberReverse) {
        return true;
    }

    return false;
}

// Starting at the largest product of two three-digit numbers, then working my
// way down finding all the palindromes and only testing that those are divisible
// by two less than four digit numbers.
int main() {
    int number = 999;
    int largestPalindromePossible = number * number;
    int largestPalindrome = largestPalindromePossible;
    bool largestPalindromeFound = false;

    while ( !largestPalindromeFound ) {
        // I worry that excessive string conversions will slowdown the runtime.
        if ( isPalindrome(largestPalindrome) ) {
            // Check if it is divisible by a number between 1 and 999
            for (int i = number; i > 2; i--) {
                if ( largestPalindrome % i == 0 ) {
                    if ( largestPalindrome / i < 1000) {
                        largestPalindromeFound = true;
                        break;
                    }
                }
            }
        }

        if (!largestPalindromeFound) { largestPalindrome--; }
    }

    cout << largestPalindrome << endl;
    exit(0);

}
