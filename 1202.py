import sys
from collections import deque
from heapq import heappush,heappop

sys_input=sys.stdin.readline

jewels=[]
bags=[]
ans=0

n,k=map(int,sys_input().rstrip().split())

for _ in range(n):
    m,v=map(int,sys_input().rstrip().split())
    jewels.append((m,v))

for _ in range(k):
    bags.append(int(sys_input()))

jewels=deque(sorted(jewels,key=lambda x:(x[0],-x[1])))
bags=deque(sorted(bags))
checks=[]

while bags:
    while jewels and jewels[0][0]<=bags[0]:
        heappush(checks,(-jewels[0][1],jewels[0][0]))
        jewels.popleft()

    if checks:
        ans+=-(heappop(checks))[0]
    bags.popleft()

print(ans)
