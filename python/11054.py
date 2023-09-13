import sys
sys_input=sys.stdin.readline

N=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))
dp=[[1]*2 for _ in range(N)]

for n in range(1,N):
    max_cur=0
    min_cur=0

    for i in range(n):
        if arr[i]<arr[n]:
            max_cur=max(dp[i][0],max_cur)
        
        if arr[N-1-i]<arr[N-1-n]:
            min_cur=max(dp[N-1-i][1],min_cur)

    if max_cur!=0:
        dp[n][0]=max_cur+1
    
    if min_cur!=0:
        dp[N-1-n][1]=min_cur+1
   
ans=0

for i in range(N):
    ans=max(ans,sum(dp[i]))

print(ans-1)