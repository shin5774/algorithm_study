import sys
sys_input=sys.stdin.readline

s=sys_input().rstrip()
es=sys_input().rstrip()
ans=[]

for x in s:
    ans.append(x)

    if ''.join(ans[-len(es):])==es:
        for _ in range(len(es)):
            ans.pop()

if len(ans)==0:
    print("FRULA")
else:
    for x in ans:
        print(x,end="")
