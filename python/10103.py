import sys
sys_input=sys.stdin.readline

a,b=100,100

for _ in range(int(sys_input())):
    x,y=map(int,sys_input().rstrip().split())

    if x>y:
        b-=x
    elif x<y:
        a-=y


print(a)
print(b)
