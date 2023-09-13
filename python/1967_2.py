import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

N=int(sys_input())

arr=[[] for _ in range(N+1)]

for _ in range(N-1):
    s,e,w=map(int,sys_input().rstrip().split())

    arr[s].append((e,w))
    arr[e].append((s,w))

def dijkstra(start):
    INF=1e8
    cost=[INF]*(N+1)
    q=[]
    heappush(q,(0,start))

    while len(q)!=0:
        c,cur=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c

        for n in arr[cur]:
            heappush(q,(c+n[1],n[0]))

    m=max(cost[1:])

    return m,cost.index(m)

s=dijkstra(1)[1]
print(dijkstra(s)[0])
