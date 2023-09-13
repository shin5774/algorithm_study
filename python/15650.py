import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

def problem(q):
    if len(q)==M:
        for x in q:
            print(x,end=" ")
        print()
        return

    for i in range(q[-1]+1,N+1):
        nq=deque(q)
        nq.append(i)
        problem(nq)


for i in range(1,N-M+2):
    q=deque()
    q.append(i)
    problem(q)
