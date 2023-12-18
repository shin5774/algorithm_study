import sys
sys_input=sys.stdin.readline

n=int(sys_input())

for _ in range(n):
    soldier=dict()
    input=list(map(int,sys_input().rstrip().split()))

    t=input[0]

    for x in input[1:]:
        if x not in soldier:
            soldier[x]=0
        soldier[x]+=1

    over=t//2
    find=False
    for x in soldier:
        if soldier[x]>over:
            print(x)
            find=True
            break

    if not find:
        print("SYJKGW")
