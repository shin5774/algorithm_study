import sys
from collections import deque

sys_input=sys.stdin.readline

n,l,r=map(int,sys_input().rstrip().split())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]
t=0

def out_range(x,y):
    if x<0 or y<0 or x==n or y==n:
        return True
    return False


def find(x,y):
    global l,r,n_arr

    s=set()
    s.add((x,y))

    q=deque()
    q.append((x,y))
    p_sum=arr[x][y]

    while q:
        cx,cy=q.popleft()

        for mv in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx,ny=cx+mv[0],cy+mv[1]

            if out_range(nx,ny) or n_arr[nx][ny]!=0 or (nx,ny) in s:
                continue

            diff=abs(arr[cx][cy]-arr[nx][ny])

            if diff>=l and diff<=r:
                q.append((nx,ny))
                s.add((nx,ny))
                p_sum+=arr[nx][ny]

    for cx,cy in s:
        n_arr[cx][cy]=p_sum//len(s)


while True:
    n_arr=[[0]*n for _ in range(n)]

    cnt=0
    for x in range(n):
        for y in range(n):
            if n_arr[x][y]==0:
                find(x,y)
                cnt+=1

    if cnt==n*n:
        break

    t+=1
    arr=n_arr

print(t)
