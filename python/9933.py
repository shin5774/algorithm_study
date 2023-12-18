import sys
sys_input=sys.stdin.readline

s=set()
ans=""

for _ in range(int(sys_input())):
    x=sys_input().rstrip()
    rx=x[::-1]

    print(x,rx)

    if x==rx or x in s:
        ans=x

    s.add(x)
    s.add(rx)


print(len(ans),ans[len(ans)//2])
