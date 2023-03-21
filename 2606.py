import sys
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())
m=int(sys_input().rstrip())

arr=[[False]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,sys_input().rstrip().split())
    arr[a][b]=True
    arr[b][a]=True

visited[1]=True

q=deque()
q.append(1)

while len(q)!=0 :
    cur=q.pop()

    for i in range(1,n+1):
        if arr[cur][i] and not visited[i]:
            visited[i]=True
            q.append(i)

sum=0

for i in range(2,n+1):
    if visited[i]:
        sum+=1

print(sum)
    

