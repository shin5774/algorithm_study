import sys
sys_input=sys.stdin.readline

L=int(sys_input())
N=int(sys_input())

cake=[0]*(L+1)
expect,expect_len=0,0
real,real_len=0,0

for i in range(1,N+1):
    p,k=map(int,sys_input().rstrip().split())

    length=k-p+1

    if length>expect_len:
        expect=i
        expect_len=length

    cur=0
    for idx in range(p,k+1):
        if cake[idx]==0:
            cake[idx]=i
            cur+=1

    if cur>real_len:
        real=i
        real_len=cur

print(expect)
print(real)
