import sys

sys_input=sys.stdin.readline

ans=[0,1,1,1,2,2,3,4,5,7,9]

for _ in range(90):
    ans.append(ans[-1]+ans[-5])

t=int(sys_input().rstrip())

for _ in range(t):
    print(ans[int(sys_input().rstrip())])
