import sys
from collections import deque
from queue import PriorityQueue

sys_input=sys.stdin.readline
MAX_COST=2000000

V,E=map(int,sys_input().rstrip().split())
start=int(sys_input())
graph=[[] for _ in range(V+1)]
cost=[MAX_COST]*(V+1)
s=set()
cost[start]=0

for _ in range(E):
    u,v,w=map(int,sys_input().rstrip().split())
    graph[u].append((v,w))

q=PriorityQueue()
q.put((0,start))

while len(s)!=V and q.qsize()!=0:
    cur_c,idx=q.get()
    if idx in s:
        continue

    s.add(idx)

    for v,c in graph[idx]:
        if v in s:
            continue

        if cost[idx]+c<cost[v]:
            cost[v]=cost[idx]+c
            q.put((cost[v],v))


for i in range(1,V+1):
    if cost[i]==MAX_COST:
        print("INF")
    else:
        print(cost[i])
