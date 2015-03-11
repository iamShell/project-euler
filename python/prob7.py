#!/usr/bin/env python

# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def isprime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

counter, i = 0, 0

while True:
    i += 1
    if isprime(i) == True:
        counter += 1
        if counter == 10001:
            print(i)
            break
