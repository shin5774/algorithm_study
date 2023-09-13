import sys
from collections import deque
from queue import PriorityQueue

sys_input=sys.stdin.readline

N=int(sys_input())
shark_size=2
count=0
fish_count=0
ans=0
arr=[]
for i in range(N):
    input=list(map(int,sys_input().rstrip().split()))
    for j in range(N):
        if input[j]==9:
            shark=(i,j)
            input[j]=0
        elif input[j]!=0:
            fish_count+=1

    arr.append(input)


def out_range(x,y):
    if x<0 or y<0 or x==N or y==N:
        return True
    return False

def bfs():
    global ans,shark,shark_size,count

    q=deque()
    q.append((shark))

    visited=[[False]*N for _ in range(N)]
    find=PriorityQueue()
    level=0
    visited[shark[0]][shark[1]]=True

    while len(q)!=0:
        cq=deque(q)
        q.clear()

        while len(cq)!=0:
            x,y=cq.pop()
            mv=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

            for nx,ny in mv:
                if out_range(nx,ny) or visited[nx][ny] or arr[nx][ny]>shark_size:
                    continue

                if arr[nx][ny]!=0 and arr[nx][ny]<shark_size:
                    find.put((nx,ny))

                q.append((nx,ny))
                visited[nx][ny]=True

        level+=1

        if find.qsize()!=0:
            x,y=find.get()
            ans+=level
            count+=1
            if count==shark_size:
                shark_size+=1
                count=0
            arr[x][y]=0
            shark=(x,y)

            return 0

    return -1


while fish_count!=0:
    if bfs()==-1:
        break
    fish_count-=1

print(ans)
