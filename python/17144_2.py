import sys
from collections import deque
sys_input=sys.stdin.readline

R,C,T=map(int,sys_input().rstrip().split())

air_cleaner=set() #r을 넣음
dust_cnt=0 #미세먼지 총량
dust=dict() #미세먼지 위치

for i in range(R):
    l=list(map(int,sys_input().rstrip().split()))

    for j in range(C):
        if l[j]==-1:
            air_cleaner.add(i)
        elif l[j]!=0:
            dust_cnt+=l[j]
            dust[(i,j)]=l[j]

def expansion():
    nextDust=dict()

    for p in dust:
        r=p[0]
        c=p[1]
        a=dust[p]

        move_cnt=0

        for nr,nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
            if nr<0 or nc<0 or nr==R or nc==C or ((nr in air_cleaner) and nc==0):
                continue

            if (nr,nc) not in nextDust:
                nextDust[(nr,nc)]=0

            nextDust[(nr,nc)]+=a//5
            move_cnt+=1

        if (r,c) not in nextDust:
            nextDust[(r,c)]=0

        nextDust[(r,c)]+=a-(a//5)*move_cnt

    return nextDust

def move():
    global dust_cnt
    moveDust=dict()

    for p in dust:
        r=p[0]
        c=p[1]
        a=dust[p]

        #오른쪽 이동
        if r in air_cleaner and c<C-1:
            moveDust[(r,c+1)]=a
        #왼쪽 이동
        elif (r==0 or r==R-1) and c!=0:
            moveDust[(r,c-1)]=a
        #윗 이동
        elif (r>max(air_cleaner) and c==0) or (r<=min(air_cleaner) and c==C-1):
            if r==max(air_cleaner)+1 and c==0:
                dust_cnt-=a
            else:
                moveDust[(r-1,c)]=a
        elif (r<min(air_cleaner) and c==0) or (r>=max(air_cleaner) and c==C-1):
            if r==min(air_cleaner)-1 and c==0:
                dust_cnt-=a
            else:
                moveDust[(r+1,c)]=a
        else:
            moveDust[(r,c)]=a

    return moveDust

for _ in range(T):
    dust=expansion()
    dust=move()

print(dust_cnt)
