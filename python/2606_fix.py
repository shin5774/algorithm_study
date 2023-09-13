import sys
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())
m=int(sys_input().rstrip())

arr=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,sys_input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

visited[1]=True
q=deque()
q.append(1)

sum=0

while len(q)!=0:
    cur=q.pop()

    for i in arr[cur]:
        if not visited[i]:
            visited[i]=True
            q.append(i)
            sum+=1

print(sum)
    

