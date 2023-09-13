import sys
from collections import deque

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

arr=[]
cnt=0
ans=0
cheese=set()

for _ in range(N):
    c_arr=list(map(int,sys_input().rstrip().split()))

    for i in range(M):
        if c_arr[i]==1:
            cnt+=1
            cheese.add((_,i))

    arr.append(c_arr)


def out_range(x,y):
    if x<0 or y<0 or x==N or y==M:
        return True
    return False

def space_checker(x,y,flag,diff):
    q=deque()
    q.append((x,y))
    arr[x][y]=flag

    while len(q)!=0:
        cx,cy=q.popleft()

        for nx,ny in [[cx+1,cy],[cx-1,cy],[cx,cy+1],[cx,cy-1]]:
            if out_range(nx,ny) or arr[nx][ny]==1:
                continue

            if diff:
                if arr[nx][ny]==flag:
                    continue
            else:
                if arr[nx][ny]!=0:
                    continue

            q.append((nx,ny))
            arr[nx][ny]=flag

    return



flag=2
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            space_checker(i,j,flag,False)
            flag+=1

while cnt!=0:
    change=set()
    n_cheese=set()

    for c in cheese:
        air_cnt=0
        for x,y in [[c[0]+1,c[1]],[c[0]-1,c[1]],[c[0],c[1]+1],[c[0],c[1]-1]]:
            if arr[x][y]==2:
                air_cnt+=1

        if air_cnt>=2:
            change.add(c)
            cnt-=1
        else:
            n_cheese.add(c)

    cheese=n_cheese

    if len(change)!=0:
        for c in change:
            space_checker(c[0],c[1],2,True)

    ans+=1

print(ans)
