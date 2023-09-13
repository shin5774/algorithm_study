import sys

sys_input=sys.stdin.readline


n=int(sys_input().rstrip())
arr=[]*n
dp=[[0]*n for _ in range(2)]

for _ in range(n):
    arr.append(int(sys_input().rstrip()))

dp[0][0]=arr[0]
dp[1][0]=arr[0]

if n>1:
    dp[0][1]=arr[0]+arr[1]
    dp[1][1]=arr[1]

for i in range(2,n):
    dp[0][i]=dp[1][i-1]+arr[i]
    dp[1][i]=max(dp[0][i-2],dp[1][i-2])+arr[i]


print(max(dp[0][n-1],dp[1][n-1]))
