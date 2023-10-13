import sys
sys_input=sys.stdin.readline

na,nb=map(int,sys_input().rstrip().split())
ss=[set(),set()]

for s in ss:
    for x in list(map(int,sys_input().rstrip().split())):
        s.add(x)

ans=sorted(list(ss[0]-ss[1]))

print(len(ans))

for x in ans:
    print(x,end=" ")
