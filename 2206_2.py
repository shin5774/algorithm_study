import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

arr=[sys_input().rstrip() for _ in range(N)]
visited=[[(0,True)]*M for _ in range(N)] #cnt,파괴가능여부
visited[0][0]=(1,True)

def out_range(x,y):
    if x<0 or y<0 or x==N or y==M:
        return True
    return False

def bfs():
    q=deque()
    q.append((0,0,True)) #x,y,벽 파괴 가능여부
    visited[0][0]=(1,True)
    while len(q)!=0:
        x,y,b=q.popleft()
        for next in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            nx=next[0]
            ny=next[1]

            if nx==N-1 and ny==M-1:
                visited[nx][ny]=(visited[x][y][0]+1,b)
                return

            if out_range(nx,ny):
                continue

            if arr[nx][ny]=='1':
                if not b or visited[nx][ny][0]!=0:
                    continue

                visited[nx][ny]=(visited[x][y][0]+1,False)
                q.append((nx,ny,False))


            elif visited[nx][ny][0]!=0:
                if visited[nx][ny][1]:
                    continue
                if not visited[nx][ny][1] and b:
                    visited[nx][ny]=(visited[x][y][0]+1,b)
                    q.append((nx,ny,b))

            else: #0이면서 방문도 안함
                visited[nx][ny]=(visited[x][y][0]+1,b)
                q.append((nx,ny,b))

bfs()
if visited[N-1][M-1][0]==0:
    print(-1)
else:
    print(visited[N-1][M-1][0])
