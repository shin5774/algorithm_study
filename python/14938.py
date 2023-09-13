import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline

ans=0
N,M,R=map(int,sys_input().rstrip().split())
INF=1e15

arr=[[] for _ in range(N+1)]
items=[0]
items+=list(map(int,sys_input().rstrip().split()))

for _ in range(R):
    a,b,c=map(int,sys_input().rstrip().split())

    arr[a].append((b,c))
    arr[b].append((a,c))


def dijkstra(start):
    cost=[INF]*(N+1)

    hq=[]
    heappush(hq,(0,start))

    while len(hq)!=0:
        c,cur=heappop(hq)

        if cost[cur]!=INF:
            continue

        cost[cur]=c

        for n in arr[cur]:
            heappush(hq,(c+n[1],n[0]))

    return cost

for i in range(1,N+1):
    cur=dijkstra(i)

    c_ans=0
    for j in range(1,N+1):
        if cur[j]<=M:
            c_ans+=items[j]

    ans=max(c_ans,ans)

print(ans)
