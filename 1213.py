import sys
from collections import deque
sys_input=sys.stdin.readline

s=sys_input().rstrip()
alpha=dict()
lim=len(s)%2
cnt=0
cor=True
find=[]
ans=deque()

for x in s:
    if x not in alpha:
        alpha[x]=0
    alpha[x]+=1

for x in alpha:
    if alpha[x]%2!=0:
        cnt+=1
        find.append(x)
        if cnt>lim:
            cor=False
            break

if cor:
    for x in find:
        ans.append(x)
        alpha[x]-=1

    for x in sorted(alpha.keys(), reverse=True):
        for _ in range(alpha[x]//2):
            ans.append(x)
            ans.appendleft(x)

    for x in ans:
        print(x,end="")
else:
    print("I'm Sorry Hansoo")
