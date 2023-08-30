import sys
from collections import deque
sys_input=sys.stdin.readline

INF=1e9
num=1
def problem(n):
    arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]
    ans=[[INF]*n for _ in range(n)]
    ans[0][0]=arr[0][0]
    q=deque()
    q.append((0,0,arr[0][0]))

    while q:
        x,y,cost=q.popleft()

        if cost>ans[x][y]:
            continue

        for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if nx<0 or ny<0 or nx==n or ny==n:
                continue

            if ans[nx][ny]>cost+arr[nx][ny]:
                q.append((nx,ny,cost+arr[nx][ny]))
                ans[nx][ny]=cost+arr[nx][ny]

    return ans[-1][-1]


while True:
    n=int(sys_input())
    if n==0:
        break
    print("Problem {}: {}".format(num,problem(n)))
    num+=1
