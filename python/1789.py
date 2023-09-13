import sys
sys_input=sys.stdin.readline

s=int(sys_input())

n=1
cur=0

while True:
    if s-cur-n<=n:
        break

    cur+=n
    n+=1

print(n)
