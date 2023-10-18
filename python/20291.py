import sys
sys_input=sys.stdin.readline

n=int(sys_input())
ans=dict()

for _ in range(n):
    input=list(map(str,sys_input().rstrip().split('.')))

    if input[1] not in ans:
        ans[input[1]]=0

    ans[input[1]]+=1

for x in sorted(ans.keys()):
    print(x,ans[x])
