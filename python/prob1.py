#!/usr/bin/env python

# This is also my FizzBuzz, but changed to do 1000 instead of 100

# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

print('Multiples of 3 and 5')
a, b = 0, 0
for i in range(0, 10):
    if i%3==0:
        a+=i
        print(i)
    if i%5==0:
        b+=i
        print(i)
#    print(a+b)
