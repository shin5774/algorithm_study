import sys
from collections import deque
sys_input=sys.stdin.readline

n=int(sys_input())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]
low,high=101,0
ans=0

for i in range(n):
    low=min(low,min(arr[i]))
    high=max(high,max(arr[i]))


def find(h):
    global n
    cnt=0
    visited=[[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]>h and not visited[i][j]:
                q=deque()
                q.append((i,j))
                visited[i][j]=True

                while q:
                    x,y=q.popleft()

                    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+d[0],y+d[1]

                        if nx<0 or ny<0 or nx==n or ny==n or visited[nx][ny] or arr[nx][ny]<=h:
                            continue

                        q.append((nx,ny))
                        visited[nx][ny]=True

                cnt+=1


    return cnt

for i in range(low-1,high):
    ans=max(ans,find(i))


print(ans)
