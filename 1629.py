import sys
from collections import deque
sys_input=sys.stdin.readline

a,b,C=map(int,sys_input().rstrip().split())


def dq(a,b):
    if b==1:
        return a%C

    if b%2==0:
        return dq(a,b//2)**2%C
    else:
        return (dq(a,b//2)*dq(a,b//2+1))%C

print(dq(a,b))