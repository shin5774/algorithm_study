import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

N,M,X=map(int,sys_input().rstrip().split())
MAX_N=10000

arr=[[] for _ in range(N+1)]
r_arr=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,sys_input().rstrip().split())
    arr[a].append((b,c))
    r_arr[b].append((a,c))


def dijkstra(start,arr):
    cost=[MAX_N]*(N+1)
    q=PriorityQueue()
    q.put((0,start))

    while q.qsize()!=0:
        c,cur=q.get()

        if cost[cur]!=MAX_N:
            continue

        cost[cur]=c

        for next in arr[cur]:
            n_cur=next[0]
            n_cost=next[1]

            q.put((c+n_cost,n_cur))

    return cost

before_cost=dijkstra(X,r_arr)
after_cost=dijkstra(X,arr)
ans=0

for i in range(1,N+1):
    ans=max(ans,before_cost[i]+after_cost[i])

print(ans)
