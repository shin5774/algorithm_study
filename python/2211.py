import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,t=map(int,sys_input().rstrip().split())
    graph[a].append((b,t))
    graph[b].append((a,t))


INF=1e8
cost=[INF]*(n+1)
q=[]
root=[[] for _ in range(n+1)]
heappush(q,(0,1,0))

while q:
    c,cur,prev=heappop(q)

    if cost[cur]!=INF:
        continue

    cost[cur]=c
    root[cur]=root[prev].copy()
    root[cur].append(cur)

    for next in graph[cur]:
        if c+next[1]<cost[next[0]]:
            heappush(q,(c+next[1],next[0],cur))

ans=set()

for i in range(2,n+1):
    for j in range(len(root[i])-1):
        if (root[i][j],root[i][j+1]) not in ans and (root[i][j+1],root[i][j]) not in ans:
            ans.add((root[i][j],root[i][j+1]))

print(len(ans))
for p in ans:
    print(p[0],p[1])
