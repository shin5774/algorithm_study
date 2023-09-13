import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())
q=PriorityQueue()

for i in range(n):
    x=int(sys_input().rstrip())

    if x==0:
        if q.qsize()==0:
            print(0)
        else:
            print(-q.get())
    else:
        q.put(-x)
