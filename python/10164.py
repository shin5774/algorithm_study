import sys,math

sys_input=sys.stdin.readline

n,m,k=map(int,sys_input().rstrip().split())

def find(sx,sy,dx,dy):
    right,down=dy-sy,dx-sx
    return math.factorial(right+down)//(math.factorial(right)*math.factorial(down))


if k==0:
    print(find(0,0,n-1,m-1))
else:
    ox,oy=k//m,k%m-1

    if oy==-1:
        ox-=1
        oy=m-1

    print(find(0,0,ox,oy)*find(ox,oy,n-1,m-1))
