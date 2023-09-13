import sys
from collections import deque
sys_input=sys.stdin.readline

N,K=map(int,sys_input().rstrip().split())
items=deque()
dp=[[0]*(N+1) for _ in range(K+1)]

items.append((0,0))

for _ in range(N):
    w,v=map(int,sys_input().rstrip().split())
    items.append((w,v))


for w in range(1,K+1):
    for idx in range(1,N+1):
        if w<items[idx][0]:
            dp[w][idx]=dp[w][idx-1]
        else:
            dp[w][idx]=max(dp[w][idx-1],dp[w-items[idx][0]][idx-1]+items[idx][1])


print(max(dp[K]))
