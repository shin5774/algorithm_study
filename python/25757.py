import sys
sys_input=sys.stdin.readline

n,game=sys_input().rstrip().split()
n=int(n)
cnt=0
ans=0
user=dict()

if game=='Y':
    player=1
elif game=='F':
    player=2
else:
    player=3


for _ in range(n):
    name=sys_input().rstrip()

    if name not in user:
        user[name]=1
        cnt+=1

    if cnt==player:
        cnt=0
        ans+=1

print(ans)
