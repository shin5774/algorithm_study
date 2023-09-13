import sys
from collections import deque

sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())
max_n=100001
arr=[0]*max_n

def input(cur,next):
    if next<0 or next>=max_n:
        return False

    if arr[next]==0:
        arr[next]=arr[cur]+1
        return True
    return False

q=deque()
q.append(n)

while len(q)!=0:
    x=q.popleft()

    if x==k:
        break

    if input(x,x+1):
        q.append(x+1)
    if input(x,x-1):
        q.append(x-1)
    if input(x,x*2):
        q.append(x*2)

print(arr[k])
