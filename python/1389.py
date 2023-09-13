import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[[False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,sys_input().rstrip().split())
    arr[a][b]=True
    arr[b][a]=True

ans,ans_cnt=0,N*N
for i in range(1,N+1):
    visited=[False]*(N+1)
    visited[i]=True

    q=deque()
    level=1
    cnt=0

    for j in range(1,N+1):
        if arr[i][j]:
            q.append(j)
            visited[j]=True

    while len(q)!=0:
        cq=deque(q)
        q=deque()

        while len(cq)!=0:
            x=cq.pop()
            cnt=cnt+level

            for j in range(1,N+1):
                if arr[x][j] and not visited[j]:
                    q.append(j)
                    visited[j]=True

        level=level+1

    if cnt<ans_cnt:
        ans_cnt=cnt
        ans=i
    elif cnt==ans_cnt and i<ans:
        ans=i

print(ans)
