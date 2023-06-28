import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

s_list=[]

l1=[]
l2=[]

for _ in range(n):
    l1.append(sys_input().rstrip())

s_list.append(set(l1))

for _ in range(m):
    l2.append(sys_input().rstrip())

s_list.append(set(l2))

ans=list(s_list[0]&s_list[1])

ans.sort()
print(len(ans))

for name in ans:
    print(name)
