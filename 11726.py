import sys

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())

ans=[]
ans.append(1)
ans.append(2)

for _ in range(2,n):
    ans.append((ans[-1]+ans[-2])%10007)

print(ans[n-1])
