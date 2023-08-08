import sys
from collections import deque
sys_input=sys.stdin.readline

N,K=map(int,sys_input().rstrip().split())

def find():
    visited=[0]*200001
    visited[N]=1 #최단시간 방문된 횟수?

    q=deque()
    q.append(N)
    t=0

    while len(q)!=0:
        cq=deque(q)
        q.clear()
        s=set() #같은 시간에 이동한 칸 확인

        while len(cq)!=0:
            x=cq.popleft()

            if x==K:
                return t,visited[K]

            for nx in [x+1,x-1,2*x]:
                if nx<0 or nx>200000:
                    continue

                if visited[nx]==0:
                    q.append(nx)
                    s.add(nx)

                if nx in s:
                    visited[nx]+=visited[x]

        t+=1


if K<=N: #뒤로가는것이 최소 시간
    print(N-K)
    print(1)
else:
    ans=find()
    for a in ans:
        print(a)
