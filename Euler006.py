# Do I even need to comment this script?
number = 100

sumOfTheSquares = 0
squareOfTheSum = 0


for i in range(1, (number + 1)):
    sumOfTheSquares += i
    squareOfTheSum += i**2

sumOfTheSquares **= 2

print sumOfTheSquares - squareOfTheSum
