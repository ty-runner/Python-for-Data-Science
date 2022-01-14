#!/usr/bin/python3
import math
n = 22
# Your code should be below this line
result = n % 7
if (result == 1) or (result == 2):
    print("Weekend")
elif ((result >= 3) and (result <= 6)) or (result == 0): 
    print("Weekday")