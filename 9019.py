import sys
from collections import deque

sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    a,b=map(int,sys_input().rstrip().split())
    visited=[False]*10000

    q=deque()
    q.append((a,""))
    visited[a]=True

    while len(q)!=0:
        n,op=q.popleft()

        d=(2*n)%10000

        if not visited[d]:
            if d==b:
                return op+"D"

            visited[d]=True
            q.append((d,op+"D"))


        if n==0:
            s=9999
        else:
            s=n-1

        if not visited[s]:
            if s==b:
                return op+"S"
            visited[s]=True
            q.append((s,op+"S"))

        #L
        l=(n*10)%10000+n//1000

        if not visited[l]:
            if l==b:
                return op+"L"
            visited[l]=True
            q.append((l,op+"L"))

        #R
        r=n//10+(n%10)*1000

        if not visited[r]:
            if r==b:
                return op+"R"
            visited[r]=True
            q.append((r,op+"R"))

for _ in range(T):
    print(problem())
