import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    n=int(sys_input())
    ans=1
    arr=dict()

    for _ in range(n):
        a,b=sys_input().rstrip().split()
        if b not in arr.keys():
            arr[b]=[]
        arr[b].append(a)

    for key in arr.keys():
        ans=ans*(len(arr[key])+1)

    return ans-1


for i in range(T):
    print(problem())
