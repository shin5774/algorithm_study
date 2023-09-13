import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline

n=int(sys_input())
arr=[]

for _ in range(n):
    heappush(arr,int(sys_input()))

ans=0

while len(arr)>1:
    a=heappop(arr)
    b=heappop(arr)

    heappush(arr,a+b)
    ans+=a+b

print(ans)
