import sys
sys_input=sys.stdin.readline

n=int(sys_input())

s=set()
ans=0

for _ in range(n):
    input=sys_input().rstrip()

    if input=='ENTER':
        ans+=len(s)
        s.clear()
    else:
        s.add(input)

ans+=len(s)

print(ans)
