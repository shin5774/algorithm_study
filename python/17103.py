import sys,math
sys_input=sys.stdin.readline

lim=1000000

prime=[True]*(lim+1)

prime[0]=prime[1]=False

for i in range(4,lim,2):
    prime[i]=False

for i in range(3,math.floor(math.sqrt(lim))+1,2):
    if not prime[i]:
        continue

    for j in range(i*i,lim,i):
        prime[j]=False

t=int(sys_input())

for _ in range(t):
    n=int(sys_input())

    cnt=0
    for i in range(2,n//2+1):
        if prime[i] and prime[n-i]:
            cnt+=1

    print(cnt)
