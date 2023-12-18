import sys,math
sys_input=sys.stdin.readline

r,c,w=map(int,sys_input().rstrip().split())
ans=0
r-=1
c-=1
for n in range(r,r+w):
    for x in range(c,c+(n-r)+1):
        ans+=math.comb(n,x)

print(ans)
