import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

arr=sorted(list(map(int,sys_input().rstrip().split())))
q=deque()
def recur(idx,level):
    if level==M:
        for x in q:
            print(x,end=" ")
        print()
        return

    for i in range(idx,N):
        q.append(arr[i])
        recur(i,level+1)
        q.pop()


for i in range(N):
    q.append(arr[i])
    recur(i,1)
    q.pop()
