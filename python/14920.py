import sys
sys_input=sys.stdin.readline

ans=1
n=int(sys_input())

while n!=1:
    if n%2==0:
        n//=2
    else:
        n=n*3+1

    ans+=1

print(ans)
