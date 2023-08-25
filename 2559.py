import sys
from heapq import heappush,heappop
from collections import deque
sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())
ans=[]
arr=deque(map(int,sys_input().rstrip().split()))
arr.appendleft(0)

for i in range(1,n+1):
    arr[i]+=arr[i-1]


for i in range(k,n+1):
    heappush(ans,-(arr[i]-arr[i-k]))

print(-heappop(ans))
