import sys
sys_input=sys.stdin.readline

r,c=map(int,sys_input().rstrip().split())
arr=[sys_input().rstrip() for _ in range(r)]
visited=[[False]*c for _ in range(r)]
ans=0

def dfs(x,y):
    global r,c

    visited[x][y]=True
    if y==c-1:
        return True

    for nx in [x-1,x,x+1]:
        if nx<0 or nx==r or visited[nx][y+1] or arr[nx][y+1]=='x':
            continue
        if dfs(nx,y+1):
            return True

    return False


for i in range(r):
    if dfs(i,0):
        ans+=1

print(ans)
