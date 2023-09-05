import sys
sys_input=sys.stdin.readline

n=int(sys_input())
lines=[]
for _ in range(n):
    a,b=map(int,sys_input().rstrip().split())
    lines.append((a,b))

lines.sort()

dp=[0]*n

for i in range(0,n):
    for j in range(0,i):
       if lines[i][1]>lines[j][1]:
           dp[i]=max(dp[i],dp[j])

    dp[i]+=1

print(n-max(dp))
