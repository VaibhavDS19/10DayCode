#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
from collections import defaultdict

def countSort(arr):
    d = defaultdict(list)
    h = len(arr)//2
    for i,(x,y) in enumerate(arr):
        d[int(x)].append("-" if i<h else y)
    for i in range(max(d)+1):
        for j in d[i]:
            yield j




if __name__ == '__main__':
    n = int(input())
    arr = [input().split() for _ in range(n)]
    print(*countSort(arr))
