import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
graph=[[] for _ in range(n+1)]
ans=[]
INF=1e8

for _ in range(m):
    a,b,t=map(int,sys_input().rstrip().split())
    graph[a].append((b,t))
    graph[b].append((a,t))


def dijkstra(x):
    cost=[INF]*(n+1)
    root=[[] for _ in range(n+1)]
    q=[]
    heappush(q,(0,x,0))

    while q:
        c,cur,prev=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c
        root[cur]=root[prev].copy()
        root[cur].append(cur)

        for next in graph[cur]:
            if cost[next[0]]>c+next[1]:
                heappush(q,(c+next[1],next[0],cur))

    l=[]

    for i in range(1,n+1):
        if i==x:
            l.append("-")
        else:
           l.append(root[i][1])

    return l


for i in range(1,n+1):
    ans.append(dijkstra(i))

for a in ans:
    for x in a:
        print(x,end=" ")
    print()
