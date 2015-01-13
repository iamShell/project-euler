#!/usr/bin/env python

# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?


def divisible1(number, x):
    for i in reversed(range(1, x+1)):
        if number % i != 0:
            return False
        return True

def divisible2(x):
    if x < 1:
        return False
    elif x == 1:
        return 1
    else:
        step = divisible2(x-1)
        number = 0
        found = False
        while not found:
            number += step
            found = divisible1(number, x)
        return number
print divisible2(20)
