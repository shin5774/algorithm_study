import sys
from collections import deque
sys_input=sys.stdin.readline

limit=210
cur=0
n=int(sys_input())

sz=int(sys_input())
arr=[sys_input().rstrip().split() for _ in range(sz)]


for t,ans in arr:
    cur+=int(t)

    if cur>=limit:
        break

    if ans=='T':
        n+=1

        if n>8:
            n=1


print(n)
