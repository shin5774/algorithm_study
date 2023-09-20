import sys
from collections import deque

sys_input=sys.stdin.readline

n,m,x,y,k=map(int,sys_input().rstrip().split())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]
mv=[[0,1],[0,-1],[-1,0],[1,0]]

r=deque([0,0,0])
c=deque([0,0,0,0])
cmd_list=list(map(int,sys_input().rstrip().split()))

#r.rotate(1) #양수:오른쪽 음수 왼

def out_range(x,y):
    if x<0 or y<0 or x==n or y==m:
        return True
    return False

for cmd in cmd_list:
    cmd-=1

    nx,ny=x+mv[cmd][0],y+mv[cmd][1]

    if out_range(nx,ny):
        continue

    if cmd==0:
        r.rotate(1)
        remain=r.popleft()
        r.appendleft(c[-1])
        c[-1]=remain
        c[1]=r[1]

    elif cmd==1:
        r.rotate(-1)
        remain=r.pop()
        r.append(c[-1])
        c[-1]=remain
        c[1]=r[1]

    elif cmd==2:
        c.rotate(-1)
        r[1]=c[1]
    else:
        c.rotate(1)
        r[1]=c[1]

    if arr[nx][ny]==0:
        arr[nx][ny]=c[-1]
    else:
        c[-1]=arr[nx][ny]
        arr[nx][ny]=0

    print(c[1])

    x,y=nx,ny
