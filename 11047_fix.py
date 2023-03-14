import sys

sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())

arr=[]
ans=0
checker=0
for i in range(n):
    a=int(sys_input().rstrip())
    if a>k:
        checker=i
        break
    arr.append(a)

for _ in range(n-checker-1):
    x=int(sys_input().rstrip())

while(k!=0):
    if k>=arr[-1]:
        ans+=k//arr[-1]
        k%=arr[-1]

    del(arr[-1])

print(ans)
