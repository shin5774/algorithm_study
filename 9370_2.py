import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline

T=int(sys_input())
INF=1e8

def dijkstra(graph,s,n):
    cost=[INF]*(n+1)
    q=[]
    heappush(q,(0,s))

    while q:
        c,cur=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c

        for next in graph[cur]:
            if cost[next[0]]>c+next[1]:
                heappush(q,(c+next[1],next[0]))

    return cost

def problem():
    n,m,t=map(int,sys_input().rstrip().split())
    s,g,h=map(int,sys_input().rstrip().split())

    graph=[[] for _ in range(n+1)]
    dest=[]
    path=0
    for _ in range(m):
        a,b,d=map(int,sys_input().rstrip().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

        if (a==g and b==h) or (a==h and b==g):
            path=d

    for _ in range(t):
        dest.append(int(sys_input()))

    dest.sort()

    start=dijkstra(graph,s,n)
    start_g=dijkstra(graph,g,n)
    start_h=dijkstra(graph,h,n)

    for x in dest:
        if (start[x]==start[h]+path+start_g[x]) or (start[x]==start[g]+path+start_h[x]):
            print(x,end=" ")

    print()

for _ in range(T):
    problem()
