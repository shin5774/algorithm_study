import sys
sys_input=sys.stdin.readline

N=int(sys_input())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
dp=[[arr[0][0],arr[0][1],arr[0][2]]]

for i in range(1,N):
    cdp=[]

    cdp.append(min(dp[i-1][1],dp[i-1][2])+arr[i][0])
    cdp.append(min(dp[i-1][0],dp[i-1][2])+arr[i][1])
    cdp.append(min(dp[i-1][0],dp[i-1][1])+arr[i][2])

    dp.append(cdp)

print(min(dp[N-1]))
