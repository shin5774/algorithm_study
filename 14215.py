import sys

sys_input=sys.stdin.readline

arr=sorted(list(map(int,sys_input().rstrip().split())))

if arr[0]+arr[1]>arr[2]:
    print(sum(arr))
else:
    print(2*(arr[0]+arr[1])-1)
