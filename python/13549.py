import sys
from collections import deque
from queue import PriorityQueue

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

def problem():
    q=PriorityQueue()
    q.put((0,N))
    m_idx=max(M,N)

    visited=[False]*(2*m_idx+1)

    while q.qsize()!=0:
        time,cur=q.get()

        if visited[cur]:
            continue

        if cur==M:
            return time

        visited[cur]=True

        if cur<=m_idx:
            q.put((time,cur*2))

        if cur>0:
            q.put((time+1,cur-1))

        if cur<2*m_idx:
            q.put((time+1,cur+1))


print(problem())
