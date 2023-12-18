import sys
sys_input=sys.stdin.readline

ans=0
cur=0
a,b,c,m=map(int,sys_input().rstrip().split())

for _ in range(24):
    if cur+a>m:
        cur=max(0,cur-c)
    else:
        cur+=a
        ans+=b

print(ans)
