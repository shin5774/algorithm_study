import sys
sys_input=sys.stdin.readline

a1,b1=map(int,sys_input().rstrip().split())
a2,b2=map(int,sys_input().rstrip().split())

def bcd(a,b):
    if b==0:
        return a
    else:
        return bcd(b,a%b)

x=a1*b2+a2*b1
y=b1*b2


if x<y:
    m=bcd(y,x)
else:
    m=bcd(x,y)

print(x//m,y//m)
