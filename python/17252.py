import sys
sys_input=sys.stdin.readline

n=int(sys_input())

if n==0:
    print("NO")
    exit()

while n:
    if n%3>1:
        break
    n//=3

if n==0:
    print("YES")
else:
    print("NO")
