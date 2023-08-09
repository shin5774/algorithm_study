import sys
from collections import deque
sys_input=sys.stdin.readline

R,C,T=map(int,sys_input().rstrip().split())

air=[] #up,down
dust=dict()

for i in range(R):
    c_arr=list(map(int,sys_input().rstrip().split()))
    for j in range(C):
        if c_arr[j]==-1:
            air.append((i,j))
        elif c_arr[j]!=0:
            dust[(i,j)]=c_arr[j]


def out_range(x,y):
    if x<0 or y<0 or x==R or y==C:
        return True
    return False

def spread():
    c_dust=dict(dust)
    dust.clear()

    for x,y in c_dust:
        mv=[[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        spread_amount=c_dust[(x,y)]//5

        if spread_amount==0:
            if (x,y) in dust:
                dust[(x,y)]+=c_dust[(x,y)]
            else:
                dust[(x,y)]=c_dust[(x,y)]

            continue

        cnt=0
        for m in mv:
            nx=m[0]
            ny=m[1]

            if out_range(nx,ny) or ((nx==air[0][0] or nx==air[1][0]) and y==0):
                continue

            cnt+=1

            if (nx,ny) in dust:
                dust[(nx,ny)]+=spread_amount
            else:
                dust[(nx,ny)]=spread_amount


        if (x,y) in dust:
            dust[(x,y)]+=c_dust[(x,y)]-spread_amount*cnt
        else:
            dust[(x,y)]=c_dust[(x,y)]-spread_amount*cnt


def circle():
    c_dust=dict(dust)
    dust.clear()

    for x,y in c_dust:
        if (x==air[0][0] or x==air[1][0]) and y>0 and y<C-1: #우측이동
            dust[(x,y+1)]=c_dust[(x,y)]

        elif (x==0 or x==R-1) and y!=0: #좌측 이동
            dust[(x,y-1)]=c_dust[(x,y)]

        elif (x>0 and x<=air[0][0] and y==C-1) or(x>air[1][0] and y==0): #상단이동
            if x==air[1][0]+1 and y==0:
                continue
            dust[(x-1,y)]=c_dust[(x,y)]

        elif (x<R-1 and x>=air[1][0] and y==C-1) or (x<air[0][0] and y==0):
            if x==air[0][0]-1 and y==0:
                continue
            dust[(x+1,y)]=c_dust[(x,y)]
        else:
            dust[(x,y)]=c_dust[(x,y)]


for _ in range(T):
    spread()
    circle()


ans=0
for v in dust.values():
    ans+=v

print(ans)
