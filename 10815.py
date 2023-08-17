import sys
sys_input=sys.stdin.readline

n=int(sys_input())
s=set(map(int,sys_input().rstrip().split()))

m=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))

for x in arr:
    if x in s:
        print(1,end=" ")
    else:
        print(0,end=" ")
