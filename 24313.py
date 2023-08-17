import sys
sys_input=sys.stdin.readline

a1,a0=map(int,sys_input().rstrip().split())
c=int(sys_input())
n0=int(sys_input())
ans=1

if (a1-c)>0:
    ans=0
elif (a1-c)==0:
    if a0>0:
        ans=0
elif (a1-c)*n0+a0>0:
    ans=0

print(ans)
