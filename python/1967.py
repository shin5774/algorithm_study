import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

N=int(sys_input())
INF=1e15

arr=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c=map(int,sys_input().rstrip().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

def dijkstra(start):
    ans=[INF]*(N+1)
    q=PriorityQueue()

    q.put((0,start))

    while q.qsize()!=0:
        cost,cur=q.get()

        if ans[cur]!=INF:
            continue

        ans[cur]=cost

        for a in arr[cur]:
            next=a[0]
            n_cost=a[1]

            q.put((cost+n_cost,next))

    max_len=max(ans[1:])
    max_idx=ans.index(max_len)

    return max_idx,max_len

a=dijkstra(1)[0]
print(dijkstra(a)[1])
