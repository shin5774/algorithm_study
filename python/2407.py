import sys,math
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
print(math.comb(n,m))
