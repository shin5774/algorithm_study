import sys
sys_input=sys.stdin.readline

t=int(sys_input())

def problem():
    n=int(sys_input())
    arr=list(map(int,sys_input().rstrip().split()))

    for i in range(1,n):
        arr[i]+=arr[i-1]
    ans=max(arr)

    for i in range(1,n):
        for j in range(i):
            ans=max(ans,arr[i]-arr[j])

    return ans

for _ in range(t):
    print(problem())
