import sys
from collections import deque
sys_input=sys.stdin.readline

n=int(sys_input())
adder=[1,5,10,50]
ans=set()
q=deque()

for x in adder:
    q.append((x,1))
    ans.add((x,1))

for i in range(n-1):
    l=len(q)

    for _ in range(l):
        x,cnt=q.popleft()

        for ad in adder:
            if (x+ad,cnt+1) in ans:
                continue
            ans.add((x+ad,cnt+1))
            q.append((x+ad,cnt+1))

        ans.remove((x,cnt))

print(len(ans))
