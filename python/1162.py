import sys
sys_input=sys.stdin.readline

n,s=map(int,sys_input().rstrip().split())
arr=list(map(int,sys_input().rstrip().split()))
ans=0

def find(cur,idx,sz):
    global ans,n,s

    if idx==n:
        if cur==s and sz!=0:
            ans+=1
        return

    find(cur+arr[idx],idx+1,sz+1)
    find(cur,idx+1,sz)

find(0,0,0)

print(ans)
