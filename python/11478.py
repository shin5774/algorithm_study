import sys

sys_input=sys.stdin.readline

s=sys_input().rstrip()
n=set()

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        n.add(s[i:j])

print(len(n))
