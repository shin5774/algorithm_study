import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

q=PriorityQueue() #정렬을 위한 PriorityQueue
n=int(sys_input().rstrip())

for _ in range(n):
    a=int(sys_input().rstrip())

    if a==0:
        if q.qsize()==0:
            print(0)
        else:
            print(q.get())
    else:
        q.put(a)
