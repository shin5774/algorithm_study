import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))

idx=-1

for i in range(n-1):
    if arr[i]>arr[i+1]:
        idx=i

if idx==-1:
    print(-1)
else:
    cur=0
    max_idx=-1
    for i in range(idx+1,n):
        if arr[i]<arr[idx] and cur<arr[i]:
            max_idx=i
            cur=arr[i]

    arr[idx],arr[max_idx]=arr[max_idx],arr[idx]
    arr[idx+1:]=sorted(arr[idx+1:],reverse=True)

    for x in arr:
        print(x,end=" ")
