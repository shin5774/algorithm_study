import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline
INF=1e15
V,E=map(int,sys_input().rstrip().split())
arr=[[] for _ in range(V+1)]

start=int(sys_input())

for _ in range(E):
    u,v,w=map(int,sys_input().rstrip().split())

    arr[u].append((v,w))

cost=[INF]*(V+1)
q=[]
heappush(q,(0,start))

while len(q)!=0:
    c,cur=heappop(q)

    if cost[cur]!=INF:
        continue
    cost[cur]=c

    for n in arr[cur]:
        heappush(q,(c+n[1],n[0]))

for i in range(1,V+1):
    if cost[i]==INF:
        print("INF")
    else:
        print(cost[i])
