import sys

sys_input=sys.stdin.readline

x=int(sys_input().rstrip())

dp=[x+1 for _ in range(x+1)]

dp[1]=0

for i in range(1,x+1):
    if(i+1<=x):
        dp[i+1]=min(dp[i]+1,dp[i+1])
    if(i*2<=x):
        dp[i*2]=min(dp[i]+1,dp[i*2])
    if(i*3<=x):
        dp[i*3]=min(dp[i]+1,dp[i*3])

print(dp[i])
