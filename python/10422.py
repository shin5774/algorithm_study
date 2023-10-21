import sys

sys_input=sys.stdin.readline

t=int(sys_input())
dp=[0]*5001
dp[0]=1

for x in range(2,5001,2):
    ans=0
    for i in range(0,x,2):
        ans+=dp[i]*dp[x-2-i]
        ans%=1000000007

    dp[x]=ans

for _ in range(t):
    l=int(sys_input())

    print(dp[l])
