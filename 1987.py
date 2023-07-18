import sys
sys_input=sys.stdin.readline

R,C=map(int,sys_input().rstrip().split())

arr=[sys_input().rstrip() for _ in range(R)]
visited=[False]*26
ans=0

def out_range(r,c):
    if r<0 or c<0 or r==R or c==C:
        return True
    return False

def dfs(r,c,level):
    global ans
    mv=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
    for m in mv:
        nr=m[0]
        nc=m[1]

        if out_range(nr,nc) or visited[ord(arr[nr][nc])-ord('A')]:
            continue

        visited[ord(arr[nr][nc])-ord('A')]=True
        dfs(nr,nc,level+1)
        visited[ord(arr[nr][nc])-ord('A')]=False
    
    ans=max(ans,level)

visited[ord(arr[0][0])-ord('A')]=True
dfs(0,0,1)
print(ans)