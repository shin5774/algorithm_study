import sys
from collections import deque

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=[]
visited=[ [False] *m  for _ in range(n+1)]
mv=[[0,-1],[0,1],[-1,0],[1,0]]
ans=1

for i in range(n):
    s=sys_input().rstrip()
    arr.append(s)

q=deque()
q.append([0,0])
visited[0][0]=True

while q:
    tq=q.copy()
    q.clear()
    find=False
    while tq:
        x,y=tq.popleft()

        if x==m-1 and y==n-1:
            find=True
            break

        for i in range(4):
            nx=x+mv[i][0]
            ny=y+mv[i][1]

            if nx>=0 and nx<m and ny>=0 and ny<n and arr[ny][nx]=='1' and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append([nx,ny])

    if find:
        break

    ans+=1

print(ans)
