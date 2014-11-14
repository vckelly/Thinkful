#!/usr/bin/env python

fizz = range(1, 101)
buzz = []

print "Fizz buzz counting up to 100"

for i in fizz:

    if not (i % 3) == 0:
        buzz += "fizz"

    if not (i % 5) == 0:
        buzz += "buzz"

    # if <something>
    # buzz += str(i)

print buzz

