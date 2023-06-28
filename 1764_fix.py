import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

a=set([sys_input().rstrip() for _ in range(n)])
b=set([sys_input().rstrip() for _ in range(m)])

ans=list(a&b)
ans.sort()

print(len(ans))

for name in ans:
    print(name)
