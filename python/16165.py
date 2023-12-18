import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

group=dict()
members=dict()

for _ in range(n):
    group_name=sys_input().rstrip()
    num=int(sys_input())
    member=[]
    for _ in range(num):
        name=sys_input().rstrip()
        member.append(name)
        members[name]=group_name

    member.sort()

    group[group_name]=member


for _ in range(m):
    problem=sys_input().rstrip()
    type=int(sys_input())

    if type==1:
        print(members[problem])
    else:
        for name in group[problem]:
            print(name)
