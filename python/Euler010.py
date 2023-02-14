primes = [True] * 2000000

for i in xrange(2, int(len(primes) ** 0.5) + 1):
    if primes[i] == True:
        for j in range(i+i, len(primes), i):
            primes[j] = False


tally = 0

for x in xrange(2, len(primes)):
    if primes[x]:
        tally += x

print tally
