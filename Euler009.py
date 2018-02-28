def f(n, m): # Equation that finds pythagorean triplets
    a = (m**2) - (n**2)
    b = (2 * m * n)
    c = (m**2) + (n**2)

    return [a, b, c]


firstCounter = 1
secondCounter = 2
success = False

while not success:
    triplet = f(firstCounter, secondCounter) # Making a triplet

    #if sum(triplet) == 1000:

    # If the sum of the values a, b, and c are a factor for 1000, you've found
    # a set that if multiplied by (1000 / sum(a, b, c), or k, will produce the
    # a, b and c value that you want. 
    if (1000.0 / sum(triplet)).is_integer():
        x = 1000 / sum(triplet)
        #print triplet[0] * triplet[1] * triplet[2]
        print ((triplet[0] * x) * (triplet[1] * x) * (triplet[2] * x))
        success = True

    secondCounter += 1

    if sum(triplet) > 1000:     # If we're finding triplets that sum up to over
        firstCounter += 1       # 1000, we have to change the parameters for the
        secondCounter = firstCounter + 1 # function to produce lower sums
