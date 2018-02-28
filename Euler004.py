from math import sqrt

firstNumber = 999 # Highest 3 digit number possible
secondNumber = 999

# No palindrome is allowed to be larger than this number
largestPossibleProduct = list(str(firstNumber * secondNumber))

firstHalfOfPalindrome = []
palindrome = []

if len(largestPossibleProduct) % 2 == 0: # If even:
    oddNumberOfDigitsInPalindrome = False

elif len(largestPossibleProduct) % 2 == 1: # If even
    oddNumberOfDigitsInPalindrome = True


for i in range(len(largestPossibleProduct) / 2):
    firstHalfOfPalindrome.append(largestPossibleProduct[i])

# Creating this variable so we can easily create the next lowest possible
# palindrome in case the palindrome being tested doesn't work
firstHalfOfPalindrome = int("".join(firstHalfOfPalindrome))


success = False

while not success:
    # We then add the second half of the palindrome to this later
    palindrome = list(str(firstHalfOfPalindrome))

    # This is just to make it easy to add the second half of the palindrome
    lengthOfFirstHalfOfPalindrome = len(str(firstHalfOfPalindrome))

    # Completing the palindrome by appending a mirror of the list to itself
    if not oddNumberOfDigitsInPalindrome:
        for i in range(lengthOfFirstHalfOfPalindrome):
            palindrome.append( palindrome[ lengthOfFirstHalfOfPalindrome - 1 - i ] )

    elif oddNumberOfDigitsInPalindrome:
        for i in range(lengthOfFirstHalfOfPalindrome - 1):
            palindrome.append( palindrome[ lengthOfFirstHalfOfPalindrome - 2 - i ] ) 
    
    # Making the palindrome an int, not a list
    palindrome = int("".join(palindrome))


    # Checking if the palindrome is GREATER than the largest possible product
    if palindrome < int("".join(largestPossibleProduct)):
        for i in range(2, int(sqrt(palindrome)) + 1): # Check if palindrome can be factored
            # Remember to make sure both factors are less than three digits
            if palindrome % i == 0 and palindrome / i <= firstNumber:
                print i
                print palindrome / i
                success = True


    # I don't THINK this will ever be needed, but I'm putting it here anyway
    # because I wanted to challenge myself
    if list(str(firstHalfOfPalindrome))[0] == '1' \
    and list(str(firstHalfOfPalindrome))[-1] == '0' \
    and oddNumberOfDigitsInPalindrome == False:
        print "The palindrome now has an odd number of digits"
        oddNumberOfDigitsInPalindrome = True
        firstHalfOfPalindrome = str(list(firstHalfOfPalindrome))
        firstHalfOfPalindrome.append('0')
        firstHalfOfPalindrome = int("".join(firstHalfOfPalindrome))

    elif list(str(firstHalfOfPalindrome))[0] == '1' \
    and list(str(firstHalfOfPalindrome))[-1] == '0' \
    and oddNumberOfDigitsInPalindrome == True:
        print "The palindrome now has an even number of digits"
        oddNumberOfDigitsInPalindrome = False
    
    # If the palindrome doesn't factor, take the first half of your original
    # Palindrome, and subract 1. For instance: 997 becomes 996, which then 
    # becomes 996699 as a palindrome
    firstHalfOfPalindrome -= 1

print palindrome
