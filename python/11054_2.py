import sys
sys_input=sys.stdin.readline

N=int(sys_input())

arr=list(map(int,sys_input().rstrip().split()))

increase=[1,]
dicrease=[0]*N
dicrease[N-1]=1

#increase
for i in range(1,N):
    cur=0
    for j in range(0,i):
        if arr[i]>arr[j]:
            cur=max(cur,increase[j])

    increase.append(cur+1)


#dicrease
for i in range(N-2,-1,-1):
    cur=0
    for j in range(N-1,i,-1):
        if arr[i]>arr[j]:
            cur=max(cur,dicrease[j])

    dicrease[i]=cur+1

ans=0
for i in range(N):
    ans=max(ans,increase[i]+dicrease[i]-1)

print(ans)
