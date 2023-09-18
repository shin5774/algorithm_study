import sys
from bisect import bisect_left

sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))
ans=[arr[0]]

for i in range(1,n):
    if ans[-1]<arr[i]:
        ans.append(arr[i])
    else:
        idx=bisect_left(ans,arr[i])
        ans[idx]=arr[i]

print(len(ans))
