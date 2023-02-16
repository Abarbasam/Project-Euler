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

int main() {
    int number = 1001;
    cout << "The number is " << number << ", is it palindromic?" << endl;
    cout << isPalindrome(1001) << endl;
}
