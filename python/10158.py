import sys
sys_input=sys.stdin.readline

w,h=map(int,sys_input().rstrip().split())
x,y=map(int,sys_input().rstrip().split())
t=int(sys_input())

def find(l,a):
    cur=(a+t)%(2*l) #시간동안 나아간 좌표 %(원위치로 올수 있는 시간)

    if cur>l: #큰경우는 역방향으로 가야함
        return 2*l-cur
    else:
        return cur

print(find(w,x),find(h,y))
