import sys
from collections import deque
from heapq import heappush,heappop

sys_input=sys.stdin.readline

N=int(sys_input())
arr=[]
fish_num=0
shark_size=2
eat_cnt=0
ans=0

for i in range(N):
    l=list(map(int,sys_input().rstrip().split()))

    for j in range(N):
        if l[j]==9:
            shark=[i,j]
        elif l[j]!=0:
            fish_num+=1

    arr.append(l)

def out_range(x,y):
    if x<0 or y<0 or x==N or y==N:
        return True
    return False

def bfs(x,y):
    global eat_cnt,shark_size,ans,fish_num

    q=deque()
    q.append((x,y)) #x,y,time
    eatable_fish=[]
    t=0
    visited=set()
    visited.add((x,y))

    while len(q)!=0 and len(eatable_fish)==0:
        cq=deque(q)
        q.clear()

        while len(cq)!=0:
            cx,cy=cq.popleft()

            for n in [[cx+1,cy],[cx-1,cy],[cx,cy+1],[cx,cy-1]]:
                nx=n[0]
                ny=n[1]

                if out_range(nx,ny) or (nx,ny) in visited or arr[nx][ny]>shark_size:
                    continue

                if arr[nx][ny]>0 and arr[nx][ny]<shark_size:
                    heappush(eatable_fish,(nx,ny))
                else:
                    q.append((nx,ny))

                visited.add((nx,ny))

        t+=1

    if len(eatable_fish)==0:
        return False

    x,y=heappop(eatable_fish)
    shark[0]=x
    shark[1]=y
    eat_cnt+=1

    arr[x][y]=0

    if eat_cnt==shark_size:
        shark_size+=1
        eat_cnt=0

    ans+=t
    fish_num-=1
    return True


arr[shark[0]][shark[1]]=0
while fish_num!=0 and bfs(shark[0],shark[1]):
    continue

print(ans)
