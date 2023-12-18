import sys
sys_input=sys.stdin.readline

arr=[True,False,False]

for _ in range(int(sys_input())):
    a,b=map(int,sys_input().rstrip().split())
    a,b=a-1,b-1

    if arr[a] or arr[b]:
        arr[a]=not arr[a]
        arr[b]=not arr[b]


for i in range(3):
    if arr[i]:
        print(i+1)
        break
