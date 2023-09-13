import sys

sys_input=sys.stdin.readline

n,m,v=map(int,sys_input().rstrip().split())

arr=[[False for _ in range(n+1)] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,sys_input().rstrip().split())
    arr[a][b]=True
    arr[b][a]=True

#dfs
def dfs(x):
    visited[x]=True
    print(x,end=" ")
    for i in range(1,n+1):
        if arr[x][i] and not visited[i]:
            dfs(i)

dfs(v)

print()

#bfs
visited=[False]*(n+1)
q=[]
q.append(v)

visited[v]=True
while len(q)!=0:
    cur_v=q[0]
    print(cur_v,end=" ")
    del(q[0])
    for i in range(1,n+1):
        if arr[cur_v][i] and not visited[i]:
            visited[i]=True
            q.append(i)
print()
