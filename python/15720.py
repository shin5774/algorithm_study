import sys
sys_input=sys.stdin.readline

a,b,c=map(int,sys_input().rstrip().split())
burgers=sorted(list(map(int,sys_input().rstrip().split())),reverse=True)
sides=sorted(list(map(int,sys_input().rstrip().split())),reverse=True)
drinks=sorted(list(map(int,sys_input().rstrip().split())),reverse=True)

sets=min(a,b,c)
sets_ans=0
ans=sum(burgers)+sum(drinks)+sum(sides)

for i in range(sets):
    sets_ans+=burgers[i]*0.9+sides[i]*0.9+drinks[i]*0.9

if a>sets:
    sets_ans+=sum(burgers[sets:])

if b>sets:
    sets_ans+=sum(sides[sets:])

if c>sets:
    sets_ans+=sum(drinks[sets:])

print(ans)
print(int(sets_ans))
