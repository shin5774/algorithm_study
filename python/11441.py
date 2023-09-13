import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))\

for i in range(1,n):
    arr[i]+=arr[i-1]

m=int(sys_input())

for _ in range(m):
    a,b=map(int,sys_input().rstrip().split())
    a,b=a-1,b-1

    if a==0:
        print(arr[b])
    else:
        print(arr[b]-arr[a-1])
