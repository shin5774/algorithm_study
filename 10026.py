import sys
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())

arr=[sys_input().rstrip() for _ in range(n)]
visited=[[False]*n for _ in range(n)]
mv=[[1,0],[-1,0],[0,1],[0,-1]]
a,b=0,0

def oor(i,j):
    if i<0 or i>=n or j<0 or j>=n:
        return True
    return False

def find(c,i,j):
    global arr,visited,mv
    q=deque()
    q.append((i,j))

    while len(q)!=0:
        ci,cj=q.pop()

        for m in mv:
            ni=ci+m[0]
            nj=cj+m[1]

            if oor(ni,nj) or visited[ni][nj] or arr[ni][nj]!=c:
                continue

            visited[ni][nj]=True
            q.append((ni,nj))

    return 0


for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        a=a+1
        find(arr[i][j],i,j)

for i in range(n):
    narr=[]
    for j in range(n):
        visited[i][j]=False
        if arr[i][j]=='G':
            narr.append('R')
        else:
            narr.append(arr[i][j])
    arr[i]=narr


for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        b=b+1
        find(arr[i][j],i,j)

print(a,b)
