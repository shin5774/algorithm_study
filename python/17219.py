import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
d=dict()

for _ in range(N):
    adr,pwd=sys_input().rstrip().split()
    d[adr]=pwd

for _ in range(M):
    a=sys_input().rstrip()
    print(d[a])
