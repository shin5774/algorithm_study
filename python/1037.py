import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=sorted(list(map(int,sys_input().rstrip().split())))

print(arr[0]*arr[-1])
