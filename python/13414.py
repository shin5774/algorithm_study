import sys
sys_input=sys.stdin.readline

k,l=map(int,sys_input().rstrip().split())
waiting=dict()

for i in range(l):
    user=sys_input().rstrip()

    waiting[user]=i

ans=list(sorted(waiting,key=lambda x:waiting[x]))

for i in range(min(k,len(ans))):
    print(ans[i])
