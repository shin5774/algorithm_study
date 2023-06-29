import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=list(map(int,sys_input().rstrip().split()))

for i in range(1,n):
    arr[i]=arr[i-1]+arr[i]

for _ in range(m):
    i,j=map(int,sys_input().rstrip().split())

    if i==1:
        print(arr[j-1])
    else:
        print(arr[j-1]-arr[i-2])
