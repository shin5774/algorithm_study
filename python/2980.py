import sys
from collections import deque
sys_input=sys.stdin.readline

n,l=map(int,sys_input().rstrip().split())
lights=deque()

for _ in range(n):
    lights.append(list(map(int,sys_input().rstrip().split())))

ans=0
cur=0

while lights:
    d,r,g=lights.popleft()

    ans+=d-cur
    cur=d

    if ans%(r+g)<=r:
        ans+=r-ans%(r+g)

ans+=l-cur

print(ans)
