import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

t=int(sys_input())
INF=1e8

def problem():
    n,d,c=map(int,sys_input().rstrip().split())

    graph=[[] for _ in range(n+1)]

    for _ in range(d):
        a,b,t=map(int,sys_input().rstrip().split())
        graph[b].append((a,t))

    q=[]
    cost=[INF]*(n+1)

    heappush(q,(0,c))

    while q:
        c,cur=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c

        for next in graph[cur]:
            heappush(q,(c+next[1],next[0]))



    cnt,time=0,0

    for i in range(1,n+1):
        if cost[i]==INF:
            continue
        cnt+=1
        time=max(time,cost[i])

    print(cnt,time)

for _ in range(t):
    problem()
