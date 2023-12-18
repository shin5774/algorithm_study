import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=[0]
cur=1
ans=0
for _ in range(n):
    arr.append(int(sys_input()))

input=[int(sys_input()) for _ in range(m)]

for x in input:
    ans+=1

    cur+=x

    if cur>=n:
        break

    cur+=arr[cur]

    if cur>=n:
        break


print(ans)
