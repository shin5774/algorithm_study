import sys

sys_input=sys.stdin.readline

N=int(sys_input())
lim=int(N**0.5)
dp=[0]*50001

for i in range(1,int(50000**0.5)+1):
    dp[i*i]=1

def find(n):
    if dp[n]!=0:
        return dp[n]

    m=5
    for i in range(int(n**0.5),0,-1):
        m=min(m,find(n-i*i))

    dp[n]=m+1

    return dp[n]

print(find(N))
