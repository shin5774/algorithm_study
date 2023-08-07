import sys
sys_input=sys.stdin.readline

N,B=map(int,sys_input().rstrip().split())
cur=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
ans=[[0]*N for _ in range(N)]

for i in range(N):
    ans[i][i]=1

def mat_cal(a,b):
    result=[[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for i in range(N):
                result[x][y]+=a[x][i]*b[i][y]
                result[x][y]=result[x][y]%1000
    return result

while B!=0:
    if B%2==0:
        cur=mat_cal(cur,cur)
        B=B//2
    else:
        ans=mat_cal(ans,cur)
        B-=1

for i in range(N):
    for j in range(N):
        print(ans[i][j],end=" ")
    print()
