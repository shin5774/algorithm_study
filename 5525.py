import sys
sys_input=sys.stdin.readline

N=int(sys_input()) #1:3 2:5 3:7
M=int(sys_input())
s=sys_input().rstrip()
i=0
ans=0

while i<M-2*N:
    if s[i]!='I':
        i=i+1
        continue

    cnt=0
    tmpi=i+1
    while s[tmpi:tmpi+2] =="OI":
        cnt=cnt+1
        tmpi=tmpi+2

    if cnt>N-1:
        ans=ans+cnt-(N-1)

    i=tmpi

print(ans)
