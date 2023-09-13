import sys
from collections import deque

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

visited=[False]*(n+1)
matrix=[[] for i in range(n+1)]
answer=0

for i in range(m):
    a,b=map(int,sys_input().rstrip().split())
    matrix[a].append(b)
    matrix[b].append(a)


for i in range(1,n+1):
    if visited[i]:
        continue
    visited[i]=True
    answer+=1

    dq=deque()

    for e in matrix[i]:
        dq.append(e)

    while len(dq)!=0:
        s=dq.pop()
        if visited[s]:
            continue
        visited[s]=True
        for e in matrix[s]:
            dq.append(e)

print(answer)
