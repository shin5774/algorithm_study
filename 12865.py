import sys
from collections import deque

sys_input=sys.stdin.readline

N,K=map(int,sys_input().rstrip().split())

weights=[0]*(N+1)
values=[0]*(N+1)
dp=[[0]*(K+1) for i in range(N+1)]

for i in range(1,N+1):
    w,v=map(int,sys_input().rstrip().split())
    weights[i]=w
    values[i]=v

for i in range(1,N+1):
    for j in range(1,K+1):
        if j<weights[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])

print(dp[N][K])
