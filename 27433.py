import sys
sys_input=sys.stdin.readline

n=int(sys_input())

if n==0 or n==1:
    print(1)

else:
    ans=1
    for i in range(2,n+1):
        ans*=i
    print(ans)
