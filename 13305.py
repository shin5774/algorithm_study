import sys
from collections import deque
sys_input=sys.stdin.readline

N=int(sys_input())
load=[0]+list(map(int,sys_input().rstrip().split()))
oil=list(map(int,sys_input().rstrip().split()))

ans=0
cur_idx=0

for i in range(1,len(load)-1):
    ans+=oil[cur_idx]*load[i]
    if oil[i]<oil[cur_idx]:
        cur_idx=i


ans+=oil[cur_idx]*load[-1]

print(ans)
