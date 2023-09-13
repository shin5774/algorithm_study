import sys
sys_input=sys.stdin.readline

N=int(sys_input())
N-=1

cur=[[1,1],[1,0]]
ans=[[1,0],[0,1]]

def mat_mul(a,b):
    result=[[0,0],[0,0]]

    for x in range(2):
        for y in range(2):
            for i in range(2):
                result[x][y]+=a[x][i]*b[i][y]
                result[x][y]%=1000000007

    return result

while N!=0:
    if N%2==0:
        cur=mat_mul(cur,cur)
        N=N//2
    else:
        ans=mat_mul(ans,cur)
        N-=1

print(ans[0][0])
