import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

s=set()
ans=0

for _ in range(N):
    s.add(sys_input().rstrip())

for _ in range(M):
    if sys_input().rstrip() in s:
        ans+=1

print(ans)
