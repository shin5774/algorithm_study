import sys
from collections import deque

sys_input=sys.stdin.readline

N,K=map(int,sys_input().rstrip().split())
visited=[[-1,0] for _ in range(200001)]

q=deque()
q.append(N)

visited[N][0]=0
visited[N][1]=1

t=0
while len(q)!=0:
    cq=deque(set(q))
    q.clear()

    while len(cq)!=0:
        p=cq.popleft()


        if p<200000 and (visited[p+1][0]==-1 or visited[p+1][0]==t+1):
            q.append(p+1)
            visited[p+1][0]=t+1
            visited[p+1][1]+=visited[p][1]
        if p>0 and (visited[p-1][0]==-1 or visited[p-1][0]==t+1):
            q.append(p-1)
            visited[p-1][0]=t+1
            visited[p-1][1]+=visited[p][1]

        if p<=100000 and (visited[2*p][0]==-1 or visited[2*p][0]==t+1):
            q.append(2*p)
            visited[2*p][0]=t+1
            visited[2*p][1]+=visited[p][1]

    if visited[K][0]!=-1:
        break
    t+=1

print(visited[K][0])
print(visited[K][1])
