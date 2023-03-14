import sys

sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())

arr=[]
ans=0

for _ in range(n):
    a=int(sys_input().rstrip())
    arr.append(a)

while(k!=0):
    if k<arr[-1]:
        del(arr[-1])
        continue

    ans+=k//arr[-1]
    k%=arr[-1]

print(ans)
