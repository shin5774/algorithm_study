import sys
from collections import deque

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[0]*100
visited=[False]*101
mv=dict()

for _ in range(N+M):
    a,b=map(int,sys_input().rstrip().split())
    mv[a]=b



q=deque()
q.append((1,0))

while len(q)!=0:
    idx,n=q.popleft()
    find=False

    for i in range(idx+1,idx+7):
        if visited[i]:
            continue

        if i==100:
            print(n+1)
            find=True
            break

        if i in mv:
            q.append((mv[i],n+1))
            visited[mv[i]]=True
        else:
            q.append((i,n+1))
            visited[i]=True

    if find:
        break
