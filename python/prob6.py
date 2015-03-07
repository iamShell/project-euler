#!/usr/bin/env python

# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
#       1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
#       (1 + 2 + ... + 10)**2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

a, b1, b2, sumsquare, sum2, = 0, 0, 1, 0, 0

for i in range(0, 100): # finds sum of first 100
    a += 1
    b1 = b1 + a
    sumsquare += a**2

sum2 = b1**2
answer = sum2 - sumsquare
print("Answer: %s" % (answer))
