import sys
from collections import deque

sys_input=sys.stdin.readline

m,n=map(int,sys_input().rstrip().split())

arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]

mv=[[1,0],[-1,0],[0,1],[0,-1]]

def BFS():
    q=deque()

    for i in range(n):
        for j in range(m):
            if(arr[i][j]==1):
                q.append([i,j])

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

    for i in range(n):
        for j in range(m):
            if(arr[i][j]==0):
                return -1

    return arr[y][x]-1

print(BFS())
