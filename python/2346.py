import sys
from collections import deque
sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))
q=deque()

for i in range(n):
    q.append((arr[i],i+1))

mv=0

while len(q)!=0:
    q.rotate(-mv)
    if q[0][0]>0:
        mv=q[0][0]-1
    else:
        mv=q[0][0]
    print(q[0][1],end=" ")
    q.popleft()
