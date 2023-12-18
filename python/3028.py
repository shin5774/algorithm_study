import sys
sys_input=sys.stdin.readline

ans=[0,1,0,0]

for x in sys_input().rstrip():
    if x=="A":
        ans[1],ans[2]=ans[2],ans[1]
    elif x=="B":
        ans[2],ans[3]=ans[3],ans[2]
    else:
        ans[1],ans[3]=ans[3],ans[1]

print(ans.index(1))
