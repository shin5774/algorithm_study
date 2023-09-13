import sys
sys_input=sys.stdin.readline

n=int(sys_input())
ans=0

for i in range(n,1,-1):
    ans+=(i-1)*(i-2)//2

print(ans)
print(3)
