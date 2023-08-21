import sys
import math
sys_input=sys.stdin.readline

lim=123456*2+1
prime=[True]*lim

prime[0]=prime[1]=False

for i in range(2,math.floor(math.sqrt(lim))+1):
    if not prime[i]:
        continue

    for j in range(i*i,lim,i):
        prime[j]=False


while True:
    n=int(sys_input())

    if n==0:
        break

    cnt=0
    for i in range(n+1,2*n+1):
        if prime[i]:
            cnt+=1

    print(cnt)
