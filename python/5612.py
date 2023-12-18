import sys
sys_input=sys.stdin.readline

n=int(sys_input())
cur=int(sys_input())
ans=cur
arr=[]

for _ in range(n):
    x,y=map(int,sys_input().rstrip().split())
    arr.append(x-y)

for x in arr:
    cur+=x
    if cur<0:
        ans=0
        break

    ans=max(ans,cur)

print(ans)
