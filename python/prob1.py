#!/usr/bin/env python

# This is also my FizzBuzz, but changed to do 1000 instead of 100

# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from sys import stdout
print('Multiples of 3 and 5')
for i in range(0,1000):
    if i%3==0:
        stdout.write('Fizz')
    if i%5==0:
        stdout.write('Buzz')
    if (i%5<>0 and i%3<>0):
        print i,
