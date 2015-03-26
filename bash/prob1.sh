#!/bin/bash

# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum=0
for j in {1..999}; do
    if [ $((j % 3)) -eq 0 ] || [ $((j % 5)) -eq 0 ]; then
        sum=$((sum+j))
    fi
done
echo $sum
