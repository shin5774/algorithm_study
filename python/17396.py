import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
goto=list(map(int,sys_input().rstrip().split()))
root=[[] for _ in range(n)]

for _ in range(m):
    a,b,t=map(int,sys_input().rstrip().split())

    if (a==n-1 or goto[a]==0) and (b==n-1 or goto[b]==0):
        root[a].append((b,t))
        root[b].append((a,t))


INF=1e12
cost=[INF]*n
q=[]
heappush(q,(0,0))

while q:
    c,cur=heappop(q)
    if cost[cur]!=INF:
        continue
    cost[cur]=c

    for next in root[cur]:
        heappush(q,(c+next[1],next[0]))


if cost[n-1]==INF:
    print(-1)
else:
    print(cost[n-1])
