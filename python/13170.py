import sys
sys_input=sys.stdin.readline

n,k,p,w=map(int,sys_input().rstrip().split())

ans=p//w

if(p%w!=0):
    ans+=1

print(ans)
