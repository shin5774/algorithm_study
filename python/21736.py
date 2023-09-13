import sys
from collections import deque

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[]
ans=0
visited=[[False]*M for _ in range(N)]
mv=[(1,0),(-1,0),(0,1),(0,-1)]

def out_range(i,j):
    if i<0 or j<0 or i==N or j==M:
        return True
    return False

q=deque()

for i in range(N):
    carr=sys_input().rstrip()

    for j in range(M):
        if carr[j] =="I":
            q.append((i,j))
            visited[i][j]=True

    arr.append(carr)

while len(q)!=0:
    cq=deque(q)
    q=deque()

    while len(cq)!=0:
        i,j=cq.pop()

        if arr[i][j]=="P":
            ans=ans+1

        for mi,mj in mv:
            ni=i+mi
            nj=j+mj

            if out_range(ni,nj) or visited[ni][nj] or arr[ni][nj]=="X":
                continue

            visited[ni][nj]=True
            q.append((ni,nj))

if ans==0:
    print("TT")
else:
    print(ans)
