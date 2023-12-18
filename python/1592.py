import sys
sys_input=sys.stdin.readline

n,m,l=map(int,sys_input().rstrip().split())
arr=[0]*(n+1)

cur=1
ans=0

while True:
    arr[cur]+=1

    if arr[cur]==m:
        break

    if arr[cur]%2==0:
        cur-=l
    else:
        cur+=l

    ans+=1

    if cur>n:
        cur-=n
    elif cur<=0:
        cur+=n


print(ans)
