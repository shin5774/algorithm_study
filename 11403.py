import sys
from collections import deque
sys_input=sys.stdin.readline

N=int(sys_input())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
ans=[]

q=deque()
for i in range(N):
    c_arr=arr[i][:]
    visited=[False]*N

    while True:
        same=True
        for j in range(N):
            if not visited[j] and c_arr[j]==1:
                q.append(j)
        n_arr=c_arr[:]

        while len(q)!=0:
            x=q.pop()
            for j in range(N):
                n_arr[j]=n_arr[j] or arr[x][j]
            visited[x]=True

        for j in range(N):
            if c_arr[j]!=n_arr[j]:
                same=False
                break
        if same:
            break
        c_arr=n_arr

    ans.append(c_arr)

for i in range(N):
    for j in range(N):
        print(ans[i][j],end=" ")
    print()
