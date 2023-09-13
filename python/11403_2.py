import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline

N=int(sys_input())
INF=1e15
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
ans=[[] for _ in range(N)]
come=[[] for _ in range(N)]


def dijkstra(n):
    cost=[INF]*N

    q=[]

    for i in range(N):
        if arr[n][i]==1:
            heappush(q,(1,i))

    while len(q)!=0:
        c,cur=heappop(q)

        if cost[cur]!=INF:
            continue

        cost[cur]=c

        for i in range(N):
            if arr[cur][i]==1:
                heappush(q,(1,i))

    return cost

for i in range(N):
    ans[i]=dijkstra(i)

for i in range(N):
    for j in range(N):
        if ans[i][j]==INF:
            ans[i][j]=0
        else:
            ans[i][j]=1

        print(ans[i][j],end=" ")
    print()
