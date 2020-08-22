#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    d%=n
    for i in range(len(a)):
        x=(i+d)%n
        if x<0:
            x+=n
        print(a[x], end=" ")
