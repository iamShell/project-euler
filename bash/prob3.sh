#!/bin/bash

# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#test number
#n=20 
n=600851475143
for (( i=2; i<=n; i++ )); do
    while [ $((n%$i)) == 0 ]; do
        echo $i
        n=$((n/$i))
    done
done

