import sys

sys_input=sys.stdin.readline

dp=[[-1]*2 for _ in range(41)]


t=int(sys_input().rstrip())
dp[0]=[1,0]
dp[1]=[0,1]

for i in range(2,41):
    dp[i]=[dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]

for _ in range(t):
    x=int(sys_input().rstrip())
    print(*dp[x])

