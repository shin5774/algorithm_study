import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

def make_set(x,m,lcm):
    s=set()
    s.add(x)

    for i in range(x+m,lcm+1,m):
        s.add(i)

    return s

def problem():
    M,N,x,y=map(int,sys_input().rstrip().split())
    if M<N:
        lcm=M*N//gcd(N,M)
    else:
        lcm=M*N//gcd(M,N)

    ans=make_set(x,M,lcm) & make_set(y,N,lcm)

    if len(ans)==0:
        return -1

    return min(ans)

for _ in range(T):
    print(problem())
