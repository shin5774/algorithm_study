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
    global n
    cost=[INF]*(n+1)
    path=[[] for _ in range(n+1)]
    q=[]
    heappush(q,(0,x,0))

    while q:
        c,cur,prev=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c
        path[cur]=path[prev].copy()
        path[cur].append(cur)

        for next in graph[cur]:
            if c+next[1]<cost[next[0]]:
                heappush(q,(c+next[1],next[0],cur))


    return path

for i in range(1,n+1):
    ans.append(dijkstra(i))

for path in ans:
    for i in range(1,n+1):
        if len(path[i])==1:
            print("-",end=" ")
        else:
            print(path[i][1],end=" ")

    print()
