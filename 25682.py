import sys
sys_input=sys.stdin.readline

n,m,k=map(int,sys_input().rstrip().split())
board=[sys_input().rstrip() for _ in range(n)]
graph=[[0]*(m+1) for _ in range(n+1)]
checker=['B','W']
ans=k*k

for i in range(n):
    for j in range(m):
        if board[i][j]==checker[(i+j)%2]:
            graph[i+1][j+1]=graph[i][j+1]+graph[i+1][j]-graph[i][j]
        else:
            graph[i+1][j+1]=graph[i][j+1]+graph[i+1][j]-graph[i][j]+1

for x in range(k,n+1):
    for y in range(k,m+1):
        cur=graph[x][y]-graph[x][y-k]-graph[x-k][y]+graph[x-k][y-k]

        ans=min(ans,min(cur,k*k-cur))

print(ans)
