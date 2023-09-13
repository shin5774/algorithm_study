import sys
sys_input=sys.stdin.readline

n,d=map(int,sys_input().rstrip().split())

graph=[]
dp=[i for i in range(10001)]

for _ in range(n):
    a,b,r=map(int,sys_input().rstrip().split())
    if b-a>r:
        graph.append((a,b,r))


for i in range(d+1):
    if i>0:
        dp[i]=min(dp[i],dp[i-1]+1)

    for g in graph:
        if g[0]==i:
            dp[g[1]]=min(dp[g[1]],dp[i]+g[2])

print(dp[d])
