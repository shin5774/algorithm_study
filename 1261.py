import sys
from collections import deque
sys_input=sys.stdin.readline

m,n=map(int,sys_input().rstrip().split())

arr=[]
dp=[[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]

for i in range(n):
    l=[]
    for x in sys_input().rstrip():
        l.append(int(x))

    arr.append(l)

def out_range(x,y):
    if x<0 or y<0 or x==n or y==m:
        return True

    return False

q=deque()
q.append((0,0))
visited[0][0]=True

while len(q)!=0:
    x,y=q.popleft()

    for mv in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx=x+mv[0]
        ny=y+mv[1]

        if out_range(nx,ny):
            continue

        if not visited[nx][ny] or dp[nx][ny]>dp[x][y]+arr[nx][ny]:
            q.append((nx,ny))
            dp[nx][ny]=dp[x][y]+arr[nx][ny]
            visited[nx][ny]=True

        #print(dp)

print(dp[n-1][m-1])
