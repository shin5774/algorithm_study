import sys
import math
sys_input=sys.stdin.readline
sys_print=sys.stdout.write
N=int(sys_input())
bottom=2*N-1

ans=[[" "]*(bottom+1) for _ in range(N+1)]

def dq(i,j,n):
    if n==3:
        ans[i][j]='*'
        ans[i+1][j-1]='*'
        ans[i+1][j+1]='*'
        for k in range(5):
            ans[i+2][j-2+k]='*'
        return
    dq(i,j,n//2)
    dq(i+n//2,j+n//2,n//2)
    dq(i+n//2,j-n//2,n//2)

dq(1,N,N)

for i in range(1,N+1):
    for j in range(1,bottom+1):
        sys_print(ans[i][j])
    sys_print('\n')
