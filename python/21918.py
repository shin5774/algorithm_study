import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
arr=list(map(int,sys_input().rstrip().split()))

for _ in range(m):
    op,l,r=map(int,sys_input().rstrip().split())

    if op==1:
        arr[l-1]=r
    elif op==2:
        for i in range(l-1,r):
            if arr[i]==1:
                arr[i]=0
            else:
                arr[i]=1
    elif op==3:
        for i in range(l-1,r):
            arr[i]=0
    else:
        for i in range(l-1,r):
            arr[i]=1

for x in arr:
    print(x,end=" ")
