import sys
from collections import deque

sys_input=sys.stdin.readline

INF=1e9

n=int(sys_input())
arr=[sys_input().rstrip() for _ in range(n)]
dp=[[INF]*n for _ in range(n)]

q=deque()
q.append((0,0,0))

while q:
    x,y,cnt=q.popleft()

    if dp[x][y]<cnt:
        continue

    for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if nx<0 or ny<0 or nx==n or ny==n:
            continue

        if arr[nx][ny]=='0':
            if dp[nx][ny]>cnt+1:
                dp[nx][ny]=cnt+1
                q.append((nx,ny,cnt+1))
        else:
            if dp[nx][ny]>cnt:
                dp[nx][ny]=cnt
                q.append((nx,ny,cnt))

print(dp[-1][-1])
