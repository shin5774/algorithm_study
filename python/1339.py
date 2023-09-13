import sys
sys_input=sys.stdin.readline

n=int(sys_input())
alpha=dict()
ans=0

for _ in range(n):
    s=sys_input().rstrip()

    for i in range(len(s)):
        if s[i] not in alpha:
            alpha[s[i]]=0
        alpha[s[i]]+=10**(len(s)-i-1)

cur=9
for x in sorted(alpha ,key=lambda x: alpha[x],reverse=True):
    ans+=alpha[x]*cur
    cur-=1

print(ans)
