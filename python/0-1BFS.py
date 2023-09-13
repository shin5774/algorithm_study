#1261번을 base로 함
import sys
from collections import deque
sys_input=sys.stdin.readline

m,n=map(int,sys_input().rstrip().split())

arr=[sys_input().rstrip() for _ in range(n)]
dp=[[n*m+1]*m for _ in range(n)]

def out_range(x,y):
    if x<0 or y<0 or x==n or y==m:
        return True

    return False

q=deque()
q.append((0,0,0))
dp[0][0]=0

while len(q)!=0:
    x,y,cnt=q.popleft()

    if cnt>dp[x][y]:
        continue

    for mv in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx=x+mv[0]
        ny=y+mv[1]

        if out_range(nx,ny):
            continue

        if arr[nx][ny]=='0':
            if dp[nx][ny]>cnt:
                q.append((nx,ny,cnt))
                dp[nx][ny]=cnt
        else:
            if dp[nx][ny]>cnt+1:
                q.appendleft((nx,ny,cnt+1))
                dp[nx][ny]=cnt+1


print(dp[n-1][m-1])
