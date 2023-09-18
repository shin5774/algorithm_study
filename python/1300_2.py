import sys
sys_input=sys.stdin.readline

n=int(sys_input())
k=int(sys_input())

low,high=1,k

def check(x):
    global k

    cnt=0

    for i in range(1,n+1):
        cnt+=min(n,mid//i)

    if cnt>=k:
        return True

    return False

while low+1<high:
    mid=(low+high)//2

    if check(mid):
        high=mid
    else:
        low=mid

print(high)
