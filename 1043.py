import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
true_people=set(list(map(int,sys_input().rstrip().split()))[1:])
party=[set(list(map(int,sys_input().rstrip().split()))[1:]) for _ in range(M)]
truth=[False]*M

while True:
    change=False

    for i in range(len(party)):
        if not truth[i] and len(party[i]&true_people)!=0:
            truth[i]=True
            true_people=true_people|party[i]
            change=True

    if not change:
        break

ans=0

for t in truth:
    if not t:
        ans+=1

print(ans)
