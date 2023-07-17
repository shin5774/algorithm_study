import sys
sys_input=sys.stdin.readline

a=sys_input().strip()
b=sys_input().strip()

arr=[[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]:
            arr[i+1][j+1]=arr[i][j]+1
        else:
            arr[i+1][j+1]=max(arr[i][j+1],arr[i+1][j])

print(arr[len(b)][len(a)])
