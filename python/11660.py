import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())

arr=[]
o_arr=[]
for i in range(N):
    carr=list(map(int,sys_input().rstrip().split()))
    ccarr=carr.copy()
    o_arr.append(ccarr)

    if i==0:
        for j in range(1,N):
            carr[j]+=carr[j-1]
    else:
        carr[0]+=arr[-1][0]

        for j in range(1,N):
            carr[j]+=(carr[j-1]+arr[-1][j]-arr[-1][j-1])

    arr.append(carr)

for _ in range(M):
    x1,y1,x2,y2=map(int,sys_input().rstrip().split())
    x1-=1
    x2-=1
    y1-=1
    y2-=1

    if x1==x2 and y1==y2:
        print(o_arr[x1][y1])
        continue

    if x1==0 and y1==0:
        print(arr[x2][y2])
    elif x1==0:
        print(arr[x2][y2]-arr[x2][y1-1])
    elif y1==0:
        print(arr[x2][y2]-arr[x1-1][y2])
    else:
        print(arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1])
