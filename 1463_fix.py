import sys

sys_input=sys.stdin.readline

x=int(sys_input().rstrip())

dp=[x+1]*(x+1)

dp[1]=0

for i in range(2,x+1):
    dp[i]=dp[i-1]+1

    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

print(dp[x])
