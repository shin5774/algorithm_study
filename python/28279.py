import sys
from collections import deque
sys_input=sys.stdin.readline

q=deque()
n=int(sys_input())

for _ in range(n):
    input=list(map(int,sys_input().rstrip().split()))

    if input[0]==1:
        q.appendleft(input[1])
    elif input[0]==2:
        q.append(input[1])
    elif input[0]==3:
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif input[0]==4:
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())
    elif input[0]==5:
        print(len(q))
    elif input[0]==6:
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif input[0]==7:
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
