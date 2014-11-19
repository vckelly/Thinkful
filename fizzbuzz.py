#!/usr/bin/env python

fizz = range(1, 101)
buzz = ""

print "Fizz buzz counting up to 100"

for i in fizz:

    if (i % 3) == 0:
        buzz += "fizz"

    if (i % 5) == 0:
        buzz += "buzz"    
    
    elif not (i % 5) == 0 and not (i % 3) == 0:
        buzz += str(i)
        
    buzz += ", "

print buzz[:-2]

