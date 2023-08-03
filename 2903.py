import sys
sys_input=sys.stdin.readline
ans=2
N=int(sys_input())

for i in range(1,N+1):
    ans+=2**(i-1)

print(ans*ans)
