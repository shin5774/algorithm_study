import sys

sys_input=sys.stdin.readline

x=0
y=1
mod=1000000007

N=int(sys_input())

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

for _ in range(N):
    b,a=map(int,sys_input().rstrip().split())
    nx=x*b+y*a
    ny=y*b

    x=nx%mod
    y=ny%mod

if x>y:
    d=gcd(x,y)
else:
    d=gcd(y,x)

x//=d
y//=d

check=mod-2
result=1

while check!=0:
    if check%2==0:
        y*=y
        y%=mod
        check//=2
    else:
        result*=y
        result%=mod
        check-=1

print(x*result%mod)
