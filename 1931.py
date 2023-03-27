import sys

sys_input=sys.stdin.readline

q=[]

n=int(sys_input().rstrip())

for _ in range(n):
    start,end=map(int,sys_input().rstrip().split())
    q.append([start,end])

q.sort(key=lambda x:x[1])

print(q)
ans=0
point=-1

for s,e in q:
    if(s>=point):
        ans+=1
        point=e

print(ans)