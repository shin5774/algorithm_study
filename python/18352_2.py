import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline
INF=1e8

n,m,k,x=map(int,sys_input().rstrip().split())

graph=[[] for _ in range(n+1)]
ans=[]

for _ in range(m):
    a,b=map(int,sys_input().rstrip().split())
    graph[a].append((b,1))


q=[]
cost=[INF]*(n+1)
heappush(q,(0,x))

while q:
    c,cur=heappop(q)

    if cost[cur]!=INF:
        continue

    cost[cur]=c

    for next in graph[cur]:
        if cost[next[0]]>c+next[1]:
            heappush(q,(c+next[1],next[0]))

for i in range(1,n+1):
    if cost[i]==k:
        ans.append(i)

if ans:
    for x in ans:
        print(x)
else:
    print(-1)
