import sys
from collections import deque
sys_input=sys.stdin.readline

s=sys_input().rstrip()
es=sys_input().rstrip()

trigger=True
while trigger and len(s)!=0:
    trigger=False
    q=[]

    for x in s:
        q.append(x)
        if "".join(q[-len(es):])==es:
            trigger=True
            for i in range(len(es)):
                q.pop()
    s=q

if len(s)==0:
    print("FRULA")

else:
    for x in s:
        print(x,end="")
