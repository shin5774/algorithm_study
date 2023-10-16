import sys
from collections import deque

sys_input=sys.stdin.readline

gears=[deque(sys_input().rstrip()) for _ in range(4)]

k=int(sys_input())

for _ in range(k):
    target,pos=map(int,sys_input().rstrip().split())
    target-=1

    #타켓 기준 왼쪽 확인
    left=[]
    for i in range(target-1,-1,-1):
        if gears[i][2]!=gears[i+1][6]:
            left.append(i)
        else:
            break

    for x in left:
        if abs(target-x)%2==0: #타겟과의 거리차를 통해 회전방향 파악
            gears[x].rotate(pos)
        else:
            gears[x].rotate(-pos)

    #타켓 기준 오른쪽 확인
    right=[]
    for i in range(target+1,4):
        if gears[i][6]!=gears[i-1][2]:
            right.append(i)
        else:
            break

    for x in right:
        if abs(target-x)%2==0:
            gears[x].rotate(pos)
        else:
            gears[x].rotate(-pos)

    #타겟 돌리기
    gears[target].rotate(pos)


ans=0

for i in range(4):
    if gears[i][0]=='1':
        ans+=2**i

print(ans)
