import sys
sys_input=sys.stdin.readline

n=int(sys_input())
ans=dict()

for _ in range(n):
    name=sys_input().rstrip()
    if name not in ans:
        ans[name]=0

    ans[name]+=1

for _ in range(n-1):
    ans[sys_input().rstrip()]-=1

for x in ans:
    if ans[x]!=0:
        print(x)
        break
