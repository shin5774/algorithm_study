import sys
sys_input=sys.stdin.readline

n=int(sys_input())
find=False
ans=dict()
ans["STRAWBERRY"]=0
ans["BANANA"]=0
ans["LIME"]=0
ans["PLUM"]=0

for _ in range(n):
    fruit,n=sys_input().rstrip().split()

    ans[fruit]+=int(n)



for x in ans:
    if ans[x]==5:
        find=True

if find:
    print("YES")
else:
    print("NO")
