import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

INF=1e8
n,m=map(int,sys_input().rstrip().split())

arr=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,sys_input().rstrip().split())

    arr[a].append((b,c))
    arr[b].append((a,c))

q=[]
cost=[INF]*(n+1)
heappush(q,(0,1))

while q:
    c,cur=heappop(q)

    if cost[cur]!=INF:
        continue

    cost[cur]=c

    for next in arr[cur]:
        heappush(q,(c+next[1],next[0]))

print(cost[n])
