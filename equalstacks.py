#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    s1=sum(h1)
    s2=sum(h2)
    s3=sum(h3)
    mina = min(s1,s2,s3)
    maxa = max(s1,s2,s3)
    while mina<maxa:
        x1=0
        x2=0
        x3=0
        if maxa==s1:
            x1=h1.pop(0)
        elif maxa==s2:
            x2=h2.pop(0)
        else:
            x3=h3.pop(0)
        s1-=x1
        s2-=x2
        s3-=x3
        mina = min(s1,s2,s3)
        maxa = max(s1,s2,s3)
    return mina

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
