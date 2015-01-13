#!/usr/bin/env python

# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

for i in range(100, 1000):
    for j in range(100, 1000):
        val = i*j
        num = "%s" % (val)
        if num == ''.join(reversed(num)):
            print(num)
            break
