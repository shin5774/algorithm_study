import sys
sys_input=sys.stdin.readline

M=int(sys_input())
mod=int(1e9+7)
a=0
b=1
def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

def cal(x,r):
    res=1

    while r!=0:
        if r%2==0:
            x=(x*x)%mod
            r//=2
        else:
            res=(res*x)%mod
            r-=1

    return res

for _ in range(M):
    n,s=map(int,sys_input().rstrip().split())
    na=(n*a+s*b)%mod
    nb=(n*b)%mod
    a=na
    b=nb

d=gcd(a,b)
a=a//d
b=b//d

print((a*cal(b,mod-2))%mod)
