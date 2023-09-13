import sys
from collections import deque

sys_input=sys.stdin.readline

W,H=map(int,sys_input().rstrip().split())

arr=[list(map(str,sys_input().rstrip())) for _ in range(H)]
dp=[[W*H]*W for _ in range(H)]
mv=[[-1,0],[0,1],[1,0],[0,-1],]

c=[]
for i in range(H):
    for j in range(W):
        if arr[i][j]=='C':
            c.append((i,j))


q=deque()
for i in range(4):
    q.append((c[0][0],c[0][1],0,i)) #위오아왼

while q:
    x,y,cnt,prev=q.popleft()

    if dp[x][y]<cnt:
        continue

    dp[x][y]=cnt

    if x==c[1][0] and y==c[1][1]:
        break

    for i in range(4):
        nx=x+mv[i][0]
        ny=y+mv[i][1]

        if nx<0 or ny<0 or nx==H or ny==W or arr[nx][ny]=='*':
            continue

        if i==prev:
            if dp[nx][ny]>dp[x][y]:
                q.appendleft((nx,ny,cnt,i))
        else:
            if dp[nx][ny]>dp[x][y]+1:
                q.append((nx,ny,cnt+1,i))


print(dp[c[1][0]][c[1][1]])
