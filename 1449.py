import sys
from collections import deque
sys_input=sys.stdin.readline

n,l=map(int,sys_input().rstrip().split())
pipe=deque(sorted(list(map(int,sys_input().rstrip().split()))))

attach=False
start=0
ans=0

while pipe:
    if not attach:
        start=pipe[0]
        ans+=1
        pipe.popleft()
        attach=True
        continue

    if pipe[0]<start+l:
        pipe.popleft()
    else:
        attach=False

print(ans)
