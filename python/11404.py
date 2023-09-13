import sys
from collections import deque
from queue import PriorityQueue

sys_input=sys.stdin.readline

N=int(sys_input())
M=int(sys_input())

arr=[[] for _ in range(N+1)]
cost=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,sys_input().rstrip().split())
    find=False

    for i in range(len(arr[a])):
        if arr[a][i]==b:
            cost[a][i]=min(cost[a][i],c)
            find=True
            break

    if not find:
        arr[a].append(b)
        cost[a].append(c)

def dijkstra(start):
    q=PriorityQueue()
    s=set()
    q.put((0,start))
    ans=[0]*(N+1)

    while q.qsize()!=0:
        c,cur=q.get()

        if cur in s:
            continue

        s.add(cur)
        ans[cur]=c

        for i in range(len(arr[cur])):
            q.put((c+cost[cur][i],arr[cur][i]))


    for x in ans[1:]:
        print(x ,end=" ")

    print()

for i in range(1,N+1):
    dijkstra(i)
