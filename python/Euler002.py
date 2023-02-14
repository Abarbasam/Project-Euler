numberCap = 4000000

fibonacciNumbers = [1, 2] # Will contain ALL fibonacci sequence numbers
evenFibonacciNumbers = [] # Will only contain even fibonacci sequence numbers

lastItemInFibonacciSequence = 1

while fibonacciNumbers[lastItemInFibonacciSequence] < numberCap:
    lastItemInFibonacciSequence = len(fibonacciNumbers) - 1
    secondLastItemInFibonacciSequence = len(fibonacciNumbers) - 2

    fibonacciNumbers.append(fibonacciNumbers[lastItemInFibonacciSequence] + \
                            fibonacciNumbers[secondLastItemInFibonacciSequence])

fibonacciNumbers.pop() # Two values will exceed the numberCap, because there
fibonacciNumbers.pop() # are two items to start. Get rid of the unneeded values

print fibonacciNumbers[-2]

for i in fibonacciNumbers: # Weeding out any number that isn't even
    if i % 2 == 0:
        evenFibonacciNumbers.append(i)

print sum(evenFibonacciNumbers) 
