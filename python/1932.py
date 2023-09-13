import sys
sys_input=sys.stdin.readline

N=int(sys_input())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
dp=[[0]*i for i in range(1, N+1)]

dp[0][0]=arr[0][0]

for n in range(1,N):
    for i in range(0,n+1):
        if i==0:
            dp[n][i]=dp[n-1][i]
        elif i==n:
            dp[n][i]=dp[n-1][i-1]
        else:
            dp[n][i]=max(dp[n-1][i-1],dp[n-1][i])

        dp[n][i]+=arr[n][i]

print(max(dp[N-1]))
