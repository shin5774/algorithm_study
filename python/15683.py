import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
arr=[]
cctv=[] #(x,y,type)
wall_cnt=0 #벽의 개수
ans=n*m
dir=[] #각 cctv의 방향을 담은 스택
mv=[[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    l=list(map(int,sys_input().rstrip().split()))

    for j in range(m):
        if l[j]>0 and l[j]<6:
            cctv.append((i,j,l[j]))
        elif l[j]==6:
            wall_cnt+=1

    arr.append(l)

def out_range(x,y):
    if x<0 or y<0 or x==n or y==m:
        return True
    return False

def draw(checker,x,y,dir): #cctv가 볼수있는 영역 표시
    while(True):
        nx,ny=x+mv[dir][0],y+mv[dir][1]

        if out_range(nx,ny) or checker[nx][ny]==6:
            return

        if checker[nx][ny]==0:
            checker[nx][ny]=-1

        x,y=nx,ny

def simulation():
    global ans,n,m,wall_cnt
    checker=[x[:] for x in arr] #배열 복사

    for i in range(len(cctv)):
        for d in dir[i]:
            draw(checker,cctv[i][0],cctv[i][1],d)

    #count
    cnt=0

    for a in checker:
        for x in a:
            if x==-1:
                cnt+=1

    ans=min(ans,n*m-len(cctv)-wall_cnt-cnt)


def back_tracking(idx):
    if idx==len(cctv):
        simulation()
        return

    if cctv[idx][2]==1:
        for d in [[0],[1],[2],[3]]: #cctv가 한번에 볼수 있는 방향
            dir.append(d)
            back_tracking(idx+1)
            dir.pop()

    elif cctv[idx][2]==2 :
        for d in [[2,3],[0,1]]:
            dir.append(d)
            back_tracking(idx+1)
            dir.pop()


    elif cctv[idx][2]==3 :
        for d in [[1,2],[0,2],[0,3],[1,3]]:
            dir.append(d)
            back_tracking(idx+1)
            dir.pop()

    elif cctv[idx][2]==4 :
        for d in [[1,2,3],[0,1,2],[0,2,3],[0,1,3]]:
            dir.append(d)
            back_tracking(idx+1)
            dir.pop()

    else:
        dir.append([0,1,2,3])
        back_tracking(idx+1)
        dir.pop()

back_tracking(0)
print(ans)
