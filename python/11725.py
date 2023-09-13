import sys
from collections import deque

sys_input=sys.stdin.readline

N=int(sys_input())
arr=[[] for _ in range(N+1)]
visited=[False]*(N+1)
ans=[0]*(N+1)

for _ in range(N-1):
    a,b=map(int,sys_input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

q=deque()

for x in arr[1]:
    q.append((x,1))

visited[1]=True

while len(q)!=0:
    x,p=q.popleft()

    ans[x]=p


    for n in arr[x]:
        if not visited[n]:
            q.append((n,x))

    visited[x]=True

for i in range(2,N+1):
    print(ans[i])
