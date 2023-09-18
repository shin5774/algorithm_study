import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
ans=0
rx,ry,rd=map(int,sys_input().rstrip().split())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
mv=[[-1,0],[0,1],[1,0],[0,-1]]

def out_range(x,y):
    if x<0 or y<0 or x==N or y==M:
        return True
    return False


def find_move():
    global rx,ry,rd

    for _ in range(4):
        rd-=1

        if rd<0:
            rd=3

        nx,ny=rx+mv[rd][0],ry+mv[rd][1]

        if out_range(nx,ny):
            continue

        if arr[nx][ny]==0:
            rx,ry=nx,ny
            return True

    return False


def check():
    global rx,ry,rd

    d=rd+2

    if d>=4:
        d-=4

    nx,ny=rx+mv[d][0],ry+mv[d][1]

    if arr[nx][ny]==1:
        return True

    rx,ry=nx,ny

    return False




while True:
    #clean
    if arr[rx][ry]==0:
        arr[rx][ry]=2
        ans+=1

    if find_move():
        continue
    elif check():
        break


print(ans)
