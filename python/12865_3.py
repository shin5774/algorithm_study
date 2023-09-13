import sys

sys_input=sys.stdin.readline

N,K=map(int,sys_input().rstrip().split())

dp=[[0]*(N+1) for _ in range(K+1)]
weight=[0]
value=[0]

for _ in range(N):
    w,v=map(int,sys_input().rstrip().split())
    weight.append(w)
    value.append(v)

for k in range(1,K+1):
    for i in range(1,N+1):
        if k<weight[i]:
            dp[k][i]=dp[k][i-1]
        else:
            dp[k][i]=max(dp[k-weight[i]][i-1]+value[i],dp[k][i-1])

print(dp[K][N])
