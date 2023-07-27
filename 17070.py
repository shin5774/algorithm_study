import sys
sys_input=sys.stdin.readline

N=int(sys_input())
arr=[[0]*(N+1) for _ in range(N+1)]
ans=0

for i in range(1,N+1):
    c_arr=list(map(int,sys_input().rstrip().split()))

    for j in range(N):
        arr[i][j+1]=c_arr[j]

def out_range(x,y):
    if x==0 or y==0 or x==N+1 or y==N+1:
        return True
    return False

def dfs(x,y,before):
    if x==N and y==N:
        global ans
        ans+=1
        return

    #가로 0
    if not (out_range(x,y+1) or arr[x][y+1]==1 or before==1):
        dfs(x,y+1,0)
    #세로 1
    if not (out_range(x+1,y) or arr[x+1][y]==1 or before==0):
        dfs(x+1,y,1)
    #대각선 2
    if not (out_range(x+1,y+1) or arr[x+1][y]==1 or arr[x][y+1]==1 or arr[x+1][y+1]==1):
        dfs(x+1,y+1,2)

dfs(1,2,0)
print(ans)
