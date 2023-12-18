import sys
from collections import deque
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
arr=[]
ans=0
cnt=1
x,y=1,1
mv=deque()
mv.append([0,1])
mv.append([1,0])
mv.append([0,-1])
mv.append([-1,0])

for i in range(n+2):
    if i==0 or i==n+1:
        l=[True]*(m+2)
    else:
        l=[False]*(m+2)
        l[0]=True
        l[m+1]=True

    arr.append(l)

while cnt<m*n:
    arr[x][y]=True
    nx,ny=x+mv[0][0],y+mv[0][1]

    if arr[nx][ny]:
        ans+=1
        mv.rotate(-1)
    else:
        x,y=nx,ny
        cnt+=1

print(ans)
