import sys
sys_input=sys.stdin.readline

n=int(sys_input())
k=int(sys_input())

start,end=1,n*n

while start<=end:
    mid=(start+end)//2

    cur=0

    for i in range(1,n+1):
        cur+=min(n,mid//i)

    if cur>=k:
        end=mid-1
    else:
        start=mid+1

print(start)
