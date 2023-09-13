import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=list(map(int,sys_input().rstrip().split()))

#1~i까지의 합을 arr[i]에 저장
for i in range(1,n):
    arr[i]=arr[i-1]+arr[i]

for _ in range(m):
    i,j=map(int,sys_input().rstrip().split())

    if i==1:
        print(arr[j-1])
    else:#두개의 값만 참조함
        print(arr[j-1]-arr[i-2])
