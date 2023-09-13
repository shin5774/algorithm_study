import sys
sys_input=sys.stdin.readline

n,c=map(int,sys_input().rstrip().split())
arr=[]
for _ in range(n):
    arr.append(int(sys_input()))

arr.sort()
start,end=1,arr[-1]-arr[0]

while start<=end:
    mid=(start+end)//2

    cnt=1
    cur=arr[0]
    for i in range(1,n):
        if arr[i]-cur<mid:
            continue
        cur=arr[i]
        cnt+=1

    #print(mid,cnt)
    if cnt>=c:
        start=mid+1
    else:
        end=mid-1


print(end)
