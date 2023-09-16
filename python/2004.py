import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

def find(x,d):
    cnt=0

    while x!=0:
        x//=d
        cnt+=x

    return cnt

up_2,up_5=find(n,2),find(n,5)
down_2,down_5=find(m,2)+find(n-m,2),find(m,5)+find(n-m,5)

two,five=up_2-down_2,up_5-down_5

if two<=0 or five<=0:
    print(0)
else:
    print(min(two,five))
