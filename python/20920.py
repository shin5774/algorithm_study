import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

d=dict()
ans=[[] for _ in range(100001)]

for _ in range(n):
    input=sys_input().rstrip()

    if len(input)<m:
        continue

    if input not in d:
        d[input]=0

    d[input]+=1

for x in d:
    heappush(ans[d[x]],(-len(x),x))


for i in range(100000,0,-1):
    while len(ans[i])!=0:
        print(heappop(ans[i])[1])
