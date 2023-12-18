import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(n)]
dp=[[arr[0][0],arr[0][1],arr[0][2]]]

for i in range(1,n):
    cur=[]
    cur.append(min(dp[-1][1],dp[-1][2])+arr[i][0])
    cur.append(min(dp[-1][0],dp[-1][2])+arr[i][1])
    cur.append(min(dp[-1][0],dp[-1][1])+arr[i][2])

    dp.append(cur)

print(min(dp[n-1]))
