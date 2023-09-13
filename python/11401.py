import sys,math
sys_input=sys.stdin.readline
p=1000000007

n,k=map(int,sys_input().rstrip().split())

def fact_mod(x):
    global p
    cur=1
    for i in range(2,x+1):
        cur*=i
        cur%=p

    return cur


a=fact_mod(n)
b=fact_mod(k)*fact_mod(n-k)
cp=p-2
cur=1
while cp>0:
    if cp%2==0:
        b*=b
        b%=p
        cp//=2
    else:
        cur*=b
        cur%=p
        cp-=1

print((a*cur)%p)
