import sys
sys_input=sys.stdin.readline

n=int(sys_input())
s=set()
s.add('ChongChong')

for _ in range(n):
    a,b=sys_input().rstrip().split()

    if a in s or b in s:
        s.add(a)
        s.add(b)

print(len(s))
