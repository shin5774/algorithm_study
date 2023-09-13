import sys
sys_input=sys.stdin.readline

x=[]
y=[]
N=int(sys_input())

for _ in range(N):
    a,b=map(int,sys_input().rstrip().split())
    x.append(a)
    y.append(b)

print(abs(max(x)-min(x))*abs(max(y)-min(y)))
