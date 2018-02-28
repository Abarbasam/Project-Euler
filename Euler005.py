number = 20

primes = [2, 3, 5, 7, 11, 13, 17, 19] # I don't want to generate the primes

def primeFactors(listOfPrimes, n):
    primeFactors = []

    fullyFactored = False

    while not fullyFactored:
        for i in primes:
            if (float(n) / i).is_integer(): # If a prime factor is found
                primeFactors.append(i)
                n = n / i # Divide the number by the prime factor

        # Eventually n becomes prime, and it is divided by itself, yielding 1.
        # Once n == 1, you know you've completely factored the number
        if n == 1: 
            fullyFactored = True

    return sorted(primeFactors)


# A list of placeholders, where item 0 represents the number 1, item 1
# represents number 2 ... And so on. [0, 1, 5] would mean that the number
# 1 occurs 0 times, the number 2 occurs 1 time, and the number 3 occurs 5 times
factorCount = [0] * number

for i in range(number):
    # Finding the factors of 1, 2, 3 ... 20
    factorsOfN = primeFactors(primes, (i+1))

    # Basic prime factorization
    for j in factorsOfN:
        count = factorsOfN.count(j) # Counting all instances of a prime factor

        # If factorCount = [0, 2], and you factor 8, you get the prime factors
        # of 2, 2 and 2. That's 2^3. Therefore, factorCount becomes [0, 3]
        if count > factorCount[j-1]: 
            factorCount[j-1] = count

answer = 1

for i in range(number):
    if factorCount[i] != 0:
        answer *= ((i+1) ** factorCount[i]) # [0, 4, 2] would result in
                                            # 2^4 + 3^2

print answer
