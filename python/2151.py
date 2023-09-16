import sys
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input())
arr=[]
door=[]
mv=[(-1,0),(0,1),(1,0),(0,-1)]
dp=[[[n*n]*n for _ in range(n)] for _ in range(4)]

for i in range(n):
    s=sys_input().rstrip()

    for j in range(n):
        if s[j]=='#':
            door.append((i,j))

    arr.append(s)

q=deque()

for i in range(4): #u,r,d,l / mirror_cnt
    q.append((door[0][0],door[0][1],i,0))

while q:
    x,y,dir,cnt=q.popleft()

    if x==door[1][0] and y==door[1][1]:
        continue

    nx,ny=x+mv[dir][0],y+mv[dir][1]

    if nx<0 or ny<0 or nx==n or ny==n or arr[nx][ny]=='*':
        continue

    if arr[nx][ny]=='!':
        for nd in [1,-1]:
            n_dir=dir+nd

            if n_dir==4:
                n_dir=0
            elif n_dir<0:
                n_dir=3

            if dp[n_dir][nx][ny]>cnt+1:
                q.append((nx,ny,n_dir,cnt+1))

            dp[n_dir][nx][ny]=cnt+1

    if dp[dir][nx][ny]>cnt:
        q.appendleft((nx,ny,dir,cnt))
        dp[dir][nx][ny]=cnt

ans=n*n

for i in range(4):
    ans=min(ans,dp[i][door[1][0]][door[1][1]])

print(ans)
