import sys
sys_input=sys.stdin.readline

n=int(sys_input())

arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]
dp=[[0]*i for i in range(1,n+1)]
dp[0][0]=arr[0][0]

for i in range(1,n):
    for j in range(0,i+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+arr[i][j]
        elif j==i:
            dp[i][j]=dp[i-1][j-1]+arr[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+arr[i][j]


print(max(dp[n-1]))
