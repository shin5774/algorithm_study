import sys
sys_input=sys.stdin.readline

N=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))
dp=[1]*N

for n in range(1,N):
    cur=0
    for i in range(0,n):
        if arr[i]<arr[n]:
            cur=max(cur,dp[i])

    if cur!=0:
        dp[n]=cur+1

print(max(dp))
