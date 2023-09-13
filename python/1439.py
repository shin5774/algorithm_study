import sys
sys_input=sys.stdin.readline

s=sys_input().rstrip()
cur=s[0]
cnt=0

for x in s:
    if x!=cur:
        cnt+=1
        cur=x

print(cnt//2+cnt%2)
