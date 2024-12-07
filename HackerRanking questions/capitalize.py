#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return s.capitalize
if __name__ == '__main__':
    fptr = open('sample.data', 'a+')

    s = input("Enter any string data: ")

    result = solve(s)

    fptr.write(str(result) + '\n')
    res = fptr.read('sample.data')
    print(res)
    fptr.close()
