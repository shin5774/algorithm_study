import sys

sys_input=sys.stdin.readline

N,B=map(int,sys_input().rstrip().split())

arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]

res=[[0]*N for _ in range(N)]

for i in range(N):
    res[i][i]=1

def mat_sum(a,b,x,y):
    ans=0

    for i in range(N):
        ans+=a[x][i]*b[i][y]

    return ans%1000


def duple(a,b):
    ans=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ans[i][j]=mat_sum(a,b,i,j)

    return ans

trigger=True

cur=arr.copy()
while B!=0:
    if B%2==0:
        cur=duple(cur,cur)
        B//=2
    else:
        res=duple(res,cur)
        B-=1

for i in range(N):
    for x in res[i]:
        print(x,end=" ")
    print()
