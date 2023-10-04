import sys
sys_input=sys.stdin.readline

n=int(sys_input())
a=int(n**0.5)

if n<=4:
    print(4)
    exit()

if a*a==n:
    print((a-1)*4)
    exit()

if n<=a*a+a:
    print(4*a-2)
else:
    print(4*a)
