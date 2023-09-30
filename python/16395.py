import sys
sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())

dp=[[0]*i for i in range(1,n+1)]

for i in range(0,n):
    for j in range(i+1):
        if j==i or j==0:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

print(dp[n-1][k-1])
