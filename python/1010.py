import sys
sys_input=sys.stdin.readline

T=int(sys_input())

dp=[[-1]*31 for _ in range(31)]

for i in range(1,31):
    dp[i][i]=1

for i in range(1,31):
    dp[1][i]=i

def find(i,j):
    if dp[i][j]!=-1:
        return dp[i][j]


    s=0
    for x in range(i-1,j):
        s+=find(i-1,x)

    dp[i][j]=s
    return s


for _ in range(T):
    n,m=map(int,sys_input().rstrip().split())

    print(find(n,m))
