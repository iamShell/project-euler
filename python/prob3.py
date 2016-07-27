#!/usr/bin/env python

# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# I had slightly more problem on this one then, overcomplicated it at first
# then rewrote it to what it currently is

# n = 20 # to test the program
n = 600851475143  # real Project Euler problem
i = 2

while i * i <= n:
    if i * i == n:
        n = i
        break

    while n % i == 0:
        n = n / i
    i = i + 1

print (n)
