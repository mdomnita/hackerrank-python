'''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    out = ''
    for l in range(len(s)):
        # capitalize only the first letter of each word or the string
        if l==0 or s[l-1]==' ':
            out += s[l].upper()
        else:
            out += s[l]
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
