import sys
sys_input=sys.stdin.readline

n=int(sys_input())

arr=[[0]*(i+1) for i in range(n+1)]
arr[0][0]=1

for i in range(1,n+1):
    for j in range(len(arr[i])):
        if j==0 or j==len(arr[i])-1:
            arr[i][j]=1
        else:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]

print(sum(arr[n]))
