import sys
from collections import deque

sys_input=sys.stdin.readline

t=int(sys_input().rstrip())

mv=[[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y,m,n):
    global arr

    q=deque()
    q.append([x,y])
    
    while(len(q)!=0):
        cx,cy=q.pop()

        for mx,my in mv:
            nx=cx+mx
            ny=cy+my

            if(nx<0 or ny<0 or nx>=m or ny>=n):
                continue
            
            if arr[ny][nx]:
                arr[ny][nx]=False
                q.append([nx,ny])



for _ in range(t):
    # m:가로 n:세로 k:입력횟수
    m,n,k=map(int,sys_input().rstrip().split())

    arr=[[False]*m for _ in range(n)]

    #배추 입력
    for _ in range(k):
        x,y=map(int,sys_input().rstrip().split())

        arr[y][x]=True

    count=0

    for i in range(n):
        for j in range(m):
            if arr[i][j]:
               arr[i][j]=False
               count+=1
               bfs(j,i,m,n) 

    print(count)