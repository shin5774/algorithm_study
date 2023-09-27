import sys
from itertools import combinations
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input())
arr=[0]+list(map(int,sys_input().rstrip().split()))
graph=[set() for i in range(n+1)]
all_node=set([i for i in range(1,n+1)])
ans=10000

def connected(nodes):
    if len(nodes)==1:
        return True

    visited=[False]*(n+1)
    q=deque()
    q.append(min(nodes))

    while q:
        cur=q.popleft()

        if visited[cur]:
            continue

        visited[cur]=True

        for next in graph[cur]:
            if not visited[next] and next in nodes:
                q.append(next)


    for x in nodes:
        if not visited[x]:
            return False

    return True


def total(nodes):
    sum=0
    for x in nodes:
        sum+=arr[x]

    return sum

for i in range(1,n+1):
    cur=list(map(int,sys_input().rstrip().split()))
    graph[i]=set(cur[1:])


for i in range(1,n//2+1):
    for cur in combinations(range(1,n+1),i):
        x_node=set(cur)
        y_node=all_node-x_node

        if not (connected(x_node) and connected(y_node)):
            continue

        cur_abs=abs(total(x_node)-total(y_node))
        if cur_abs<ans:
            ans=cur_abs


if ans==10000:
    print(-1)
else:
    print(ans)
