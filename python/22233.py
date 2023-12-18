import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
ans=set()

for _ in range(n):
    ans.add(sys_input().rstrip())


for _ in range(m):
    input=sys_input().rstrip().split(",")

    for x in input:
        if x in ans:
            ans.remove(x)

    print(len(ans))
