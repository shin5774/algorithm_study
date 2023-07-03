import sys
from collections import deque

sys_input=sys.stdin.readline

m,n,h=map(int,sys_input().rstrip().split())

arr=[]
mv=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
q=deque()
answer=0

def out_range(x,y,z):
    global m,n,h
    if x<0 or x>=m or y<0 or y>=n or z<0 or z>=h:
        return False
    return True

for k in range(h): #�迭 �Է°���
    tarr=[]

    for j in range(n):
        carr=list(map(int,sys_input().rstrip().split()))

        for i in range(len(carr)): #���� �丶���� ��ġ�� Q�� �ִ´�.
            if carr[i]==1:
                q.append((i,j,k))

        tarr.append(carr)

    arr.append(tarr)

while len(q)!=0: #BFS
    cq=deque(q)
    nq=deque()
    while len(cq)!=0:
        cx,cy,cz=cq.pop()

        for tx,ty,tz in mv:
            nx=cx+tx
            ny=cy+ty
            nz=cz+tz

            if not out_range(nx,ny,nz) or arr[nz][ny][nx]!=0:
                continue

            arr[nz][ny][nx]=1
            nq.append((nx,ny,nz))

    q=deque(nq)
    if len(q)==0: #answer���� ����+1�� �Ǵ°��� ����
        break
    answer=answer+1

#������ �丶���� ���翩�� Ȯ��
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] ==0:
                answer=-1

print(answer)
