import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    n=int(sys_input())

    arr=[]

    for _ in range(n):
        a,b=map(int,sys_input().rstrip().split())
        arr.append((a,b))

    arr.sort()

    ans=1
    idx=0

    for i in range(1,n):
        if arr[idx][1]>arr[i][1]:
            idx=i
            ans+=1

    return ans



for _ in range(T):
    print(problem())
