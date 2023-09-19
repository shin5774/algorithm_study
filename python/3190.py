import sys
from collections import deque
sys_input=sys.stdin.readline

n=int(sys_input())
k=int(sys_input())
arr=[[0]*n for _ in range(n)]
mv=[[-1,0],[0,1],[1,0],[0,-1]]
change_dir=deque()
snake_pos=deque()
t=0
dir=1 #위부터 90도 +1
s_len=1

def out_range(x,y):
    if x<0 or y<0 or x==n or y==n:
        return True

    return False

for _ in range(k):
    i,j=map(int,sys_input().rstrip().split())
    arr[i-1][j-1]=1

l=int(sys_input())

for _ in range(l):
    ct,cd=map(str,sys_input().rstrip().split())
    change_dir.append((ct,cd))

arr[0][0]=-1
snake_pos.append((0,0))

while True:
    t+=1
    #move
    x,y=snake_pos[-1][0],snake_pos[-1][1]

    nx,ny=x+mv[dir][0],y+mv[dir][1]

    if out_range(nx,ny) or arr[nx][ny]==-1:
        break

    #check
    if arr[nx][ny]!=1:
        lx,ly=snake_pos[0][0],snake_pos[0][1]
        arr[lx][ly]=0
        snake_pos.popleft()

    arr[nx][ny]=-1

    #change
    snake_pos.append((nx,ny))

    #direction
    if change_dir and int(change_dir[0][0])==t:
        if change_dir[0][1]=='L':
            dir-=1
            if dir<0:
                dir=3
        else:
            dir+=1
            if dir==4:
                dir=0

        change_dir.popleft()


print(t)
