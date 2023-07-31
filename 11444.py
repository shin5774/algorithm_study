import sys
sys_input=sys.stdin.readline

arr=[[1,1],[1,0]]
f1=1
f0=0
N=int(sys_input())
N-=1

def mat_cal(a,b,x,y):
    ans=0

    for i in range(2):
        ans+=a[x][i]*b[i][y]

    return ans%1000000007


def mat_mul(a,b):
    ans=[[] for _ in range(2)]

    for x in range(2):
        for y in range(2):
            ans[x].append(mat_cal(a,b,x,y))

    return ans

res=[[1,0],[0,1]]

while N!=0:
    if N%2==0:
        arr=mat_mul(arr,arr)
        N=N//2
    else:
        res=mat_mul(res,arr)
        N-=1

print(res[0][0])
