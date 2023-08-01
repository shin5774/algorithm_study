import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
ans=0
s=set()

def dfs(x,y,level):
    global ans

    if level==4:
        cur=0
        for i,j in s:
            cur+=arr[i][j]
        cur+=arr[x][y]

        if ans<cur:
            ans=cur

        return

    s.add((x,y))

    for e in s:
        for nx,ny in [[e[0]+1,e[1]],[e[0]-1,e[1]],[e[0],e[1]+1]]:
            if  nx<0 or ny<0 or nx==N or ny==M or (nx,ny) in s:
                continue
            dfs(nx,ny,level+1)

    s.remove((x,y))


for i in range(N):
    for j in range(M):
        dfs(i,j,1)

print(ans)
