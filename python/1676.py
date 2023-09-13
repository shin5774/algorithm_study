import sys

sys_input=sys.stdin.readline

check=[0,0]
n=int(sys_input().rstrip())

for i in range(n,1,-1):
    while i%2==0:
        check[0]+=1
        i/=2

    while i%5==0:
        check[1]+=1
        i/=5

print(min(check))
