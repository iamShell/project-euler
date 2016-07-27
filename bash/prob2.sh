#!/bin/bash

a=0; b=1; x=0; y=0; 
while true; do
    a=$((a+b))
    b=$((b+a))
    if [ $((a % 2)) -eq 0 ]; then
        x=$((x+a))
        echo $x
    fi
    if [ $((b % 2)) -eq 0 ]; then
        y=$((y+b))
        echo $y
    fi
    if [ $((b)) -gt 4000000 ]; then
        echo $((x+y))
        break
    fi
done
