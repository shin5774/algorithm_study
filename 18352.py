import sys
from collections import deque
sys_input=sys.stdin.readline

INF=1e8
N,M,K,X=map(int,sys_input().rstrip().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    s,e=map(int,sys_input().rstrip().split())
    graph[s].append(e)

q=deque()
visited=[INF]*(N+1)
q.append(X)
visited[X]=0
level=1

while q:
    l=len(q)

    for _ in range(l):
        cur=q.popleft()

        for n in graph[cur]:
            if visited[n]==INF:
                q.append(n)
                visited[n]=level

    level+=1

ans=[]

for i in range(1,N+1):
    if visited[i]==K:
        ans.append(i)

if ans:
    for x in ans:
        print(x)
else:
    print(-1)
