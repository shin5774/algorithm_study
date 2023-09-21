import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=sorted(list(map(int,sys_input().rstrip().split())))
ans=1

for x in arr:
    if ans<x:
        break
    ans+=x

print(ans)
