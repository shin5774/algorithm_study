import sys
sys_input=sys.stdin.readline

n,x,k=map(int,sys_input().rstrip().split())

arr=[False]*(n+1)
arr[x]=True

for _ in range(k):
    a,b=map(int,sys_input().rstrip().split())

    arr[a],arr[b]=arr[b],arr[a]


for i in range(1,n+1):
    if arr[i]:
        print(i)
        break
