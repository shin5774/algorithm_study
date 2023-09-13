import sys
from collections import deque

sys_input=sys.stdin.readline

po=[]
ne=[]

ans=0

n=int(sys_input())

for _ in range(n):
    x=int(sys_input())

    if x>0:
        po.append(x)
    else:
        ne.append(x)

po=deque(sorted(po))
ne=deque(sorted(ne,reverse=True))

while len(po)>1:
    a=po.pop()
    b=po.pop()

    if a==1 or b==1:
        ans+=a+b
    else:
        ans+=a*b

if po:
    ans+=po[0]

while len(ne)>1:
    a=ne.pop()
    b=ne.pop()

    ans+=a*b

if ne:
    ans+=ne[0]

print(ans)
