import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

V=int(sys_input())

arr=[[] for _ in range(V+1)]

for _ in range(V):
    line=list(map(int,sys_input().rstrip().split()))

    root=line[0]
    for i in range(1,len(line)-1,2):
        arr[root].append((line[i],line[i+1]))
        arr[line[i]].append((root,line[i+1]))

def dijkstra(start):
    cost=[1e15]*(V+1)
    q=PriorityQueue()
    q.put((0,start))

    while q.qsize()!=0:
        c,cur=q.get()

        if cost[cur]!=1e15:
            continue

        cost[cur]=c

        for n in arr[cur]:
            q.put((c+n[1],n[0]))

    max_num=max(cost[1:])
    max_idx=cost.index(max_num)

    return max_num,max_idx

ans=dijkstra(dijkstra(1)[1])[0]

print(ans)
