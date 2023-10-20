import sys
sys_input=sys.stdin.readline

dp=dict() #n의 값이 상당히 커서 불필요한 공간 낭비를 줄이기 위해 dict를 사용
dp[0]=1

n,p,q=map(int,sys_input().rstrip().split())

def find(x): #dynamic programming
    if x not in dp:
        dp[x]=find(x//p)+find(x//q)

    return dp[x]

print(find(n))
