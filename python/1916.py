import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

N=int(sys_input())
M=int(sys_input())

arr=[[] for _ in range(N+1)]
cost=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,sys_input().rstrip().split())

    idx=-1

    for i in range(len(arr[a])):
        if arr[a][i]==b:
            idx=i
            break

    if idx!=-1:
        cost[a][idx]=min(cost[a][idx],c)

    else:
        arr[a].append(b)
        cost[a].append(c)

def dijkstra(start,end):
    ans=[-1]*(N+1)
    q=PriorityQueue()
    q.put((0,start))

    while q.qsize()!=0:
        c,cur=q.get()

        if ans[cur]!=-1:
            continue

        ans[cur]=c

        for i in range(len(arr[cur])):
            q.put((c+cost[cur][i],arr[cur][i]))


    return ans[end]

start,end=map(int,sys_input().rstrip().split())
print(dijkstra(start,end))
