import sys
sys_input=sys.stdin.readline

ans=dict()

for _ in range(int(sys_input())):
    for i in [4,6,4,10]:

        for x in sys_input().rstrip().split():
            if x=='-':
                continue

            if x not in ans:
                ans[x]=0
            ans[x]+=i

if len(ans.keys())==0:
    print("Yes")
    exit()

if max(ans.values())-min(ans.values())<=12:
    print("Yes")
else:
    print("No")
