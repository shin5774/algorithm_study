import sys
from itertools import combinations
from collections import deque

sys_input=sys.stdin.readline
N,M=map(int,sys_input().rstrip().split())
arr=[]
virus=[]
total_remain=0
empty=[]
ans=0

for i in range(N):
    l=list(map(int,sys_input().rstrip().split()))

    for j in range(M):
        if l[j]==2:
            virus.append((i,j))
        elif l[j]==0:
            empty.append((i,j))
            total_remain+=1

    arr.append(l)

print
def find(walls):
    global total_remain,virus,arr

    visit=[[False]*M for _ in range(N)]

    for x,y in walls:
        visit[x][y]=True

    q=deque()
    remain=total_remain

    for v in virus:
        q.append(v)

    while len(q)!=0:
        x,y=q.popleft()

        for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if nx<0 or ny<0 or nx==N or ny==M or arr[nx][ny]!=0 or visit[nx][ny]:
                continue

            q.append((nx,ny))
            visit[nx][ny]=True
            remain-=1

        if remain<ans:
            return 0

    return remain


for walls in list(combinations(empty,3)):
    ans=max(ans,find(walls))

print(ans-3)
