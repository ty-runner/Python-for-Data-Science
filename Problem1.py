#!/usr/bin/python3
import math #Used for math properties to find a Fibonacci number
number = 5 #Test number
# Your code should be below this line
if (number % 2 == 0) and ((5 * number^2 + 4) or (5 * number^2 - 4)): #If (even) and (first Fibonacci condition\ 
#OR second Fibonacci condition)
    print("Yes")
else:
    print("No")