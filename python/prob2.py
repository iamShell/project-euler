#!/usr/bin/env python

# Even Fibonacci numbers
# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# def fib():
#     a = 0
#     b = 1
#     while True:
#         yield a # 0 to start with
#         a, b = b, a + b
#
# for index, fibonacci in enumerate(fib()):
#     print('%s' % (index))
#
#     if index == 4000:
#         break


a, b = 0, 1
x, y = 0, 0
while True:
    a = a + b
    b = b + a
    if a % 2 == 0:
        x += a
        print(x)
    if b % 2 == 0:
        y += b
        print(y)
    if b > 4000000:
        print(x+y)
        break
