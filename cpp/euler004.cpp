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

// Exhaustive search of all combinations 
int main() {
    int number = 999;
    int largestPalindrome = 0;
    int mult = 0;

    for (int i = number; i > 0; i--) {
        for (int j = i; j > 0; j--) {
            mult = i * j;
            if ( isPalindrome(mult) ) {
                if (largestPalindrome < mult) largestPalindrome = mult; 
            }
        }
    }

    cout << largestPalindrome << endl;
}
