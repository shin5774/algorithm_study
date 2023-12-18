import sys
sys_input=sys.stdin.readline

t=int(sys_input())

def problem(n):
    ans=n


    while(n!=1):
        if n%2==0:
            n//=2
        else:
            n=n*3+1
            ans=max(ans,n)

    print(ans)


for _ in range(t):
    problem(int(sys_input()))
