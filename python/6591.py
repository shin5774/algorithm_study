import sys,math
sys_input=sys.stdin.readline

while True:
    n,k=map(int,sys_input().rstrip().split())

    if n==0 and k==0:
        break

    print(math.comb(n,k))
