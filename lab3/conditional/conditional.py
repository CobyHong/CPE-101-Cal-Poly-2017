import math

def max_101(a,b):
    max = a
    if (a>b):
        max = a
    else:
        max = b
    return max

def max_of_three(a,b,c):
    max = a
    if (a>=b) and (a>=c):
        max = a
    if (b>=c) and (b>=a):
        max = b
    if (c>=a) and (c>=b):
        max = c
    return max

def rental_late_fee(numdays):
    if (numdays<=0):
        return 0
    elif (numdays<=9):
        return 5
    elif (numdays<=15):
        return 7
    elif (numdays<=24):
        return 19
    elif (numdays>24):
        return 100

