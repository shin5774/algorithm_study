import sys
from collections import deque
sys_input=sys.stdin.readline

q=deque()
n=int(sys_input())

is_q=list(map(int,sys_input().rstrip().split()))

arr=list(map(int,sys_input().rstrip().split()))

for i in range(n):
    if is_q[i]==0:
        q.append(arr[i])

m=int(sys_input())

for x in list(map(int,sys_input().rstrip().split())):
    if len(q)==0:
        print(x,end=" ")
        continue

    print(q.pop(),end=" ")
    q.appendleft(x)
