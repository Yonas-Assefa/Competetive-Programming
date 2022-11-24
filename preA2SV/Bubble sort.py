#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    numSwaps =0
    swap_happen=True
    while(swap_happen):
        swap_happen=False
        iteration=0
        for j in range(n-1-iteration):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                numSwaps +=1
                iteration+=1
                swap_happen=True
    print(f"Array is sorted in {numSwaps} swaps.") 
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

                
    
