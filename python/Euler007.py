# It's not great, but my other script didn't work.
# This is easy to follow

primes = [2, 3, 5]

multipleOfSix = 6
operandSwitcher = 1

success = False
while not success:
    if operandSwitcher == -1:
        multipleOfSix += 6

    # All primes are multiples of 6 plus or minus 1
    primes.append(multipleOfSix + (1 * operandSwitcher))
    operandSwitcher *= -1
    
    # Simple seive, which gets rid of any non-prime numbers in the list
    for i in range(len(primes) - 2):
        if primes[-1] % primes[i] == 0:
            primes.pop()


    if len(primes) >= 10001:
        success = True

print primes[10000]
