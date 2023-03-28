import sys
from collections import deque

sys_input=sys.stdin.readline

m,n=map(int,sys_input().rstrip().split())

arr=[]
q=deque()

mv=[[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    arr_input=list(map(int,sys_input().rstrip().split()))
    for j in range(m):
        if(arr_input[j]==1):
            q.append([i,j])
    arr.append(arr_input)

while len(q)!=0:
    y,x=q.popleft()

    for my,mx in mv:
        tx=x+mx
        ty=y+my

        if tx<0 or ty<0 or tx>=m or ty>=n:
            continue

        if arr[ty][tx]!=0:
            continue

        arr[ty][tx]=arr[y][x]+1
        q.append([ty,tx])

ans=-1

for i in range(n):
    checker=False
    for j in range(m):
        if arr[i][j]==0:
            checker=True
            break
        ans=max(ans,arr[i][j])
    if checker:
        ans=0
        break


print(ans-1)
