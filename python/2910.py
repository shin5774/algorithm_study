import sys
sys_input=sys.stdin.readline

n,c=map(int,sys_input().rstrip().split())
d=dict()

for x in list(map(int,sys_input().rstrip().split())):
    if x not in d:
        d[x]=0
    d[x]+=1

for x in sorted(d.keys(),key=lambda x:d[x],reverse=True): #value를 기준으로 내림차순 정렬
    for _ in range(d[x]):
        print(x,end=" ")
