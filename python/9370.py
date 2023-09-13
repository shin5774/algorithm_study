import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline

T=int(sys_input())
INF=1e9

def dijkstra(n,s):
    global graph

    q=[]
    cost=[INF]*(n+1)

    heappush(q,(0,s))

    while q:
        c,cur=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c

        for next in graph[cur]:
            heappush(q,(c+next[1],next[0]))

    return cost



def problem():
    global graph
    n,m,t=map(int,sys_input().rstrip().split())
    s,g,h=map(int,sys_input().rstrip().split())

    graph=[[] for _ in range(n+1)]
    goals=[]

    for _ in range(m):
        a,b,d=map(int,sys_input().rstrip().split())

        graph[a].append((b,d))
        graph[b].append((a,d))

        if (a==g and b==h) or(a==h and b==g):
            p=d

    for _ in range(t):
        goals.append(int(sys_input()))

    goals.sort()

    start=dijkstra(n,s)
    bet_h=dijkstra(n,h)
    bet_g=dijkstra(n,g)

    ans=[]

    for x in goals:
        if start[x]==start[g]+p+bet_h[x] or start[x]==start[h]+p+bet_g[x]:
            ans.append(x)


    for x in ans:
        print(x,end=" ")
    print()


for _ in range(T):
    problem()
