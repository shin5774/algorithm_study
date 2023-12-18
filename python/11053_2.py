import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))
dp=[1]

for i in range(1,n):
    find=0
    for j in range(i):
        if arr[i]>arr[j]:
            find=max(find,dp[j])

    dp.append(find+1)

print(max(dp))
