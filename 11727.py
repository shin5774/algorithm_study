import sys

sys_input=sys.stdin.readline

arr=[0,1,3]

n=int(sys_input().rstrip())

for _ in range(3,n+1):
    arr.append((2*arr[-2]+arr[-1])%10007)

print(arr[n])
