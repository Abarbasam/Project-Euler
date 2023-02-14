# This script is poorly built, but I'm too lazy to make it better

number = 600851475143
possiblePrimes = [2, 3]

for i in range(1, 1500):
    possiblePrimes.append(i * 6 - 1) # All primes are multiples of six plus
    possiblePrimes.append(i * 6 + 1) # or minus 1

        
for i in range(len(possiblePrimes) - 1):
    sieveNumber = possiblePrimes[i]
    
    # Checking if any items in the list are divisible by other primes
    # If they are, get rid of them, they are NOT prime
    for j in range((i+1), len(possiblePrimes)):
        if possiblePrimes[j] % sieveNumber == 0:
            possiblePrimes.pop(j)

            # Replacing non-prime values with 2 makes it so the loop does 
            # not go out-of-range.
            possiblePrimes.insert(j, 2)

      
primes = [2]

# all values of 2 are removed, leaving us with only primes
for i in possiblePrimes:
    if i != 2:
        primes.append(i)

success = False
iterator = len(primes) - 1

# Checking if our number divides by any prime in the list
while not success:
    if number % primes[iterator] == 0:
        success = True
        print primes[iterator]
    elif iterator != 0:
        iterator -= 1
