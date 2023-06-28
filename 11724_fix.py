import sys
from collections import deque

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=[[]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m): #인접행렬
    a,b=map(int,sys_input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

ans=0

def bfs(x): #BFS
    q=deque()
    q.append(x)

    while len(q)!=0:
        c=q.pop()
        for n in arr[c]:
            if not visited[n]:
                visited[n]=True
                q.append(n)

for i in range(1,n+1):
    if not visited[i]:
        ans+=1
        bfs(i)

print(ans)
