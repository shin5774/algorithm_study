import sys
sys.setrecursionlimit(1000)
sys_input=sys.stdin.readline

R,C=map(int,sys_input().rstrip().split())
arr=[]
dx,dy=[1,-1,0,0],[0,0,1,-1]

for _ in range(R):
    l=sys_input().rstrip()
    c=[]
    for i in range(C):
        c.append(ord(l[i])-ord('A'))

    arr.append(c)
ans=0
visited=[False]*(ord('Z')-ord('A')+1)

def dfs(x,y,level):
    global ans
    if ans==26:
        return

    for sx,sy in zip(dx,dy):
        nx=x+sx
        ny=y+sy
        if nx<0 or ny<0 or nx==R or ny==C or visited[arr[nx][ny]]:
            continue

        visited[arr[nx][ny]]=True
        dfs(nx,ny,level+1)
        visited[arr[nx][ny]]=False

    ans=max(ans,level)

visited[arr[0][0]]=True
dfs(0,0,1)
print(ans)
