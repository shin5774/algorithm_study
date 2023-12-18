import sys
sys_input=sys.stdin.readline

a,b,c=map(int,sys_input().rstrip().split())

arr=[0]*101

for _ in range(3):
    s,e=map(int,sys_input().rstrip().split())

    for t in range(s,e):
        arr[t]+=1


ans=0

for i in range(101):
    if arr[i]==1:
        ans+=a
    elif arr[i]==2:
        ans+=b*2
    elif arr[i]==3:
        ans+=c*3


print(ans)
