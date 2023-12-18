import sys
from collections import deque

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
ans=[[-1]*m for _ in range(n)]
clouds=deque()

for i in range(n):
    l=sys_input().rstrip()

    for j in range(m):
        if l[j]=='c':
            clouds.append((i,j,0))


while clouds:
    x,y,cur=clouds.popleft()

    if ans[x][y]!=-1:
        continue

    ans[x][y]=cur

    if y+1==m:
        continue

    clouds.append((x,y+1,cur+1))


for l in ans:
    for x in l:
        print(x,end=" ")
    print()
