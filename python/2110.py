import sys
sys.setrecursionlimit(10**8)
sys_input=sys.stdin.readline

n,c=map(int,sys_input().rstrip().split())
arr=[]
ans=0

for _ in range(n):
    arr.append(int(sys_input()))

arr.sort()

low,high=1,1000000000

while low<=high:
    mid=(low+high)//2

    cnt=0
    idx=0

    for i in range(1,n):
        if arr[i]-arr[idx]>=mid:
            cnt+=1
            idx=i

    if cnt<c-1:
        high=mid-1
    else:
        ans=mid
        low=mid+1


print(ans)
