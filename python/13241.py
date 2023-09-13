import sys
sys_input=sys.stdin.readline

a,b=map(int,sys_input().rstrip().split())

def bcd(a,b):
    if b==0:
        return a
    return bcd(b,a%b)

if a<b:
    m=bcd(b,a)
else:
    m=bcd(a,b)

print(a*b//m)
