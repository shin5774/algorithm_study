import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=[int(sys_input()) for _ in range(n)]
ans=0

for i in range(n-1):
    for j in range(i,-1,-1):
        if arr[j+1]<=arr[j]:
            ans+=arr[j]-(arr[j+1]-1)
            arr[j]=arr[j+1]-1

print(ans)
