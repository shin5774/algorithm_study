import sys
from queue import PriorityQueue
sys_input=sys.stdin.readline

Q=PriorityQueue()

N=int(sys_input())

for _ in range(N):
    x=int(sys_input())

    if x==0:
        if Q.qsize()==0:
            print(0)
        else:
            print(Q.get()[1])
    else:
        Q.put((abs(x),x))
