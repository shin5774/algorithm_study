import sys
from bisect import bisect_left
sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))
lis=[]
lis.append(arr[0])

for i in range(1,n):
    if lis[-1]<arr[i]:
        lis.append(arr[i])
        continue
    idx=bisect_left(lis,arr[i])
    lis[idx]=arr[i]

print(len(lis))
