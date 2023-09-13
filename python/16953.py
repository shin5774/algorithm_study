import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline
A,B=map(int,sys_input().rstrip().split())


def problem():
    q=PriorityQueue()
    q.put((0,A))
    while q.qsize()!=0:
        c,cur=q.get()

        if cur==B:
            return c+1

        if cur*2<=B:
            q.put((c+1,cur*2))

        n=int(str(cur)+"1")
        if n<=B:
            q.put((c+1,n))

    return -1


print(problem())
