import sys

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())

arr=list(map(int,sys_input().rstrip().split()))

arr.sort()

sum=0
for i in range(n,0,-1):
    sum+=arr[n-i]*i

print(sum)
