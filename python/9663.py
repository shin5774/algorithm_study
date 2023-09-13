import sys
from collections import deque

sys_input=sys.stdin.readline

N=int(sys_input())
ans=0

def check(i,j,pi,pj):
    if j==pj or abs(i-pi)==abs(j-pj):
        return True
    return False

def problem(q):
    c_idx=len(q)

    if c_idx==N:
        global ans
        ans+=1
        return

    for i in range(N):
        can_place=True
        for pi,pj in q:
            if check(c_idx,i,pi,pj):
                can_place=False
                break

        if can_place:
            nq=deque(q)
            nq.append((c_idx,i))
            problem(nq)

for i in range(N):
    q=deque()
    q.append((0,i))
    problem(q)

print(ans)
