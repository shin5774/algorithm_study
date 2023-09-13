import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    N=int(sys_input())
    arr=[list(map(int,sys_input().rstrip().split())) for _ in range(2)]
    dp=[[0]*N for _ in range(3)]
    dp[0][0]=arr[0][0]
    dp[1][0]=arr[1][0]

    for i in range(1,N):
        dp[0][i]=max(dp[1][i-1],dp[2][i-1])+arr[0][i]
        dp[1][i]=max(dp[0][i-1],dp[2][i-1])+arr[1][i]
        dp[2][i]=max(dp[0][i-1],dp[1][i-1])

    print(max(dp[0][N-1],dp[1][N-1],dp[2][N-1]))

for _ in range(T):
    problem()
