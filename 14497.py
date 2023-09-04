import sys
from collections import deque
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
x1,y1,x2,y2=map(int,sys_input().rstrip().split())

arr=[sys_input().rstrip() for _ in range(n)]
visited=[[n*m]*m for _ in range(n)]
q=deque()
q.append((x1-1,y1-1,0))
visited[x1-1][y1-1]=0

while q:
    x,y,cnt=q.popleft()

    if x==x2-1 and y==y2-1:
        break

    for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if nx<0 or ny<0 or nx==n or ny==m:
            continue

        if arr[nx][ny]=='1':
            if visited[nx][ny]>visited[x][y]+1:
                q.append((nx,ny,cnt+1))
                visited[nx][ny]=cnt+1
        else:
            if visited[nx][ny]>visited[x][y]:
                q.appendleft((nx,ny,cnt))
                visited[nx][ny]=cnt



print(visited[x2-1][y2-1]+1)
