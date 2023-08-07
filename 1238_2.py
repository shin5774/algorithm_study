import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

N,M,X=map(int,sys_input().rstrip().split())
INF=1e8
arr=[[] for _ in range(N+1)]
r_arr=[[] for _ in range(N+1)]
ans=0

for _ in range(M):
    a,b,t=map(int,sys_input().rstrip().split())

    arr[a].append((b,t))
    r_arr[b].append((a,t))

def dijkstra(arr,start):
    ans=[INF]*(N+1)
    hq=[]
    heappush(hq,(0,start))

    while len(hq)!=0:
        cost,cur=heappop(hq)

        if ans[cur]!=INF:
            continue

        ans[cur]=cost

        for n in arr[cur]:
            heappush(hq,(cost+n[1],n[0]))

    return ans

x_find=dijkstra(r_arr,X)
find=dijkstra(arr,X)

for i in range(1,N+1):
    ans=max(ans,x_find[i]+find[i])

print(ans)
