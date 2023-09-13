import sys
sys_input=sys.stdin.readline
sys_print=sys.stdout.write

N=int(sys_input())

ans=[[" "]*(2*N+1) for _ in range(N)]

def divide(n,p):
    if n==3:
        x,y=p

        ans[x][y]='*'
        ans[x+1][y-1]='*'
        ans[x+1][y+1]='*'

        for t in range(y-2,y+3):
            ans[x+2][t]='*'

        return

    divide(n//2,p)
    divide(n//2,(p[0]+n//2,p[1]-n//2))
    divide(n//2,(p[0]+n//2,p[1]+n//2))


divide(N,(0,N-1))

for i in range(N):
    for j in range(2*N+1):
        sys_print(ans[i][j])
    sys_print('\n')
