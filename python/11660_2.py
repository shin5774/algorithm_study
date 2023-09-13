import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

arr=[]*N

l=list(map(int,sys_input().rstrip().split()))

for i in range(1,N):
    l[i]+=l[i-1]

arr.append(l)

for i in range(1,N):
    l=list(map(int,sys_input().rstrip().split()))

    l[0]+=arr[i-1][0]

    for j in range(1,N):
        l[j]+=l[j-1]+arr[i-1][j]-arr[i-1][j-1]

    arr.append(l)

for _ in range(M):
    x1,y1,x2,y2=map(int,sys_input().rstrip().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1

    if x1==0:
        if y1==0:
            print(arr[x2][y2])
        else:
            print(arr[x2][y2]-arr[x2][y1-1])
    elif y1==0:
        print(arr[x2][y2]-arr[x1-1][y2])
    else:
        print(arr[x2][y2]-arr[x2][y1-1]-arr[x1-1][y2]+arr[x1-1][y1-1])
