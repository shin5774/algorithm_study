import sys
from itertools import combinations

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
house=[]
chicken=[]
ans=101*201

def problem(chickens):
    global ans
    sum=0
    for x,y in house:
        cur=101
        for cx,cy in chickens:
            cur=min(cur,abs(x-cx)+abs(y-cy))

        sum+=cur
        if sum>ans:
            return
    ans=sum

for i in range(N):
    l=list(map(int,sys_input().rstrip().split()))
    for j in range(N):
        if l[j]==1:
            house.append((i,j))
        elif l[j]==2:
            chicken.append((i,j))


c_list=list(combinations(chicken,M))


for chickens in c_list:
    problem(chickens)

print(ans)
