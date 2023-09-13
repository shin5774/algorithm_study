import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

N,E=map(int,sys_input().rstrip().split())

arr=[[] for _ in range(N+1)]

for _ in range(E):
    a,b,c=map(int,sys_input().rstrip().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

v1,v2=map(int,sys_input().rstrip().split())

def dijkstra(start):
    q=PriorityQueue()
    ans=[-1]*(N+1)
    q.put((0,start))

    while q.qsize()!=0:
        cost,idx=q.get()

        if ans[idx]!=-1:
            continue

        ans[idx]=cost

        for t in arr[idx]:
            next=t[0]
            n_cost=t[1]

            q.put((cost+n_cost,next))

    return ans

one=dijkstra(1)
r1=dijkstra(v1)
r2=dijkstra(v2)
ans=-1

if r1[v2]!=-1:
    exist=False
    if one[v1]!=-1 and r2[N]!=-1:
        exist=True
        ans=one[v1]+r1[v2]+r2[N]

    if one[v2]!=-1 and r1[N]!=-1:
        if exist:
            ans=min(ans,one[v2]+r2[v1]+r1[N])
        else:
            ans=one[v2]+r2[v1]+r1[N]

print(ans)
