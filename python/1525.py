import sys
from collections import deque
sys_input=sys.stdin.readline

find='123456780'
arr=''

#arr 만들기,join으로 간단하게 만들수 있음
for i in range(3):
    l=list(map(int,sys_input().rstrip().split()))
    for j in range(3):
        if l[j]==0:
            pos=i*3+j

        arr+=str(l[j])

s=set()
q=deque()
q.append((arr,0,pos)) #cnt

while q:
    cur,cnt,pos=q.popleft()

    if cur in s:
        continue

    s.add(cur)

    if cur==find:
        print(cnt)
        exit()

    x,y=pos//3,pos%3

    for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if nx<0 or ny<0 or nx==3 or ny==3:
            continue

        npos=nx*3+ny
        next=''

        #여기도 join으로 쉽게 만들기 가능(str->list후 위치변경후 ->str)
        for i in range(9):
            if i==pos:
                next+=cur[npos]
            elif i==npos:
                next+=cur[pos]
            else:
                next+=cur[i]

        q.append((next,cnt+1,nx*3+ny))


print(-1)
