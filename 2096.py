import sys
sys_input=sys.stdin.readline

N=int(sys_input())

min_dp=[]
max_dp=[]

arr=list(map(int,sys_input().rstrip().split()))

for i in range(3):
    min_dp.append(arr[i])
    max_dp.append(arr[i])

for i in range(1,N):
    n_min_dp=[]
    n_max_dp=[]

    arr=list(map(int,sys_input().rstrip().split()))

    n_min_dp.append(min(min_dp[0],min_dp[1])+arr[0])
    n_max_dp.append(max(max_dp[0],max_dp[1])+arr[0])
    n_min_dp.append(min(min_dp[0],min_dp[1],min_dp[2])+arr[1])
    n_max_dp.append(max(max_dp[0],max_dp[1],max_dp[2])+arr[1])
    n_min_dp.append(min(min_dp[1],min_dp[2])+arr[2])
    n_max_dp.append(max(max_dp[1],max_dp[2])+arr[2])

    min_dp=n_min_dp
    max_dp=n_max_dp

print(max(max_dp),min(min_dp))
