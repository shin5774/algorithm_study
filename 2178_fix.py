import sys
from collections import deque

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=[]
mv=[[0,-1],[0,1],[-1,0],[1,0]]


for _ in range(n):
    arr.append(list(map(int,sys_input().rstrip())))

q=deque()
q.append([0,0])

while q:
    x,y=q.popleft()

    if x==m-1 and y==n-1:
        print(arr[y][x])
        break

    for i in range(4):
        nx=x+mv[i][0]
        ny=y+mv[i][1]

        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue

        if arr[ny][nx]==1:
            arr[ny][nx]=arr[y][x]+1
            q.append([nx,ny])
