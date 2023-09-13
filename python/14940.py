import sys
from collections import deque

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
q=deque()
arr=[]
level=0
ans=[[0]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]
mv=[(1,0),(-1,0),(0,1),(0,-1)]

def out_range(i,j):
    if i<0 or j<0 or i>=N or j>=M:
        return True
    return False

for i in range(N):
    carr=list(map(int,sys_input().rstrip().split()))
    for j in range(M):
        if carr[j] == 2:
            q.append((i,j))
            visited[i][j]=True
    arr.append(carr)

while len(q)!=0:
    cq=deque(q)
    q=deque()
    while len(cq)!=0:
        i,j=cq.pop()
        ans[i][j]=level

        for mi,mj in mv:
            ni=i+mi
            nj=j+mj

            if out_range(ni,nj) or visited[ni][nj] or arr[ni][nj]==0:
                continue

            visited[ni][nj]=True
            q.append((ni,nj))

    level=level+1


for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j]==1:
            print(-1,end=" ")
        else:
            print(ans[i][j],end=" ")

    print()
