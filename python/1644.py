import sys
sys_input=sys.stdin.readline

n=int(sys_input())
is_prime=[True]*(n+1)
is_prime[0]=is_prime[1]=False
prime=[]
ans=0
for i in range(4,n,2):
    is_prime[i]=False

for i in range(3,int(n**0.5)+2,2):
    if is_prime[i]:
        for j in range(i*i,n+1,i):
            is_prime[j]=False

if n>=2:
    prime.append(2)
    for i in range(3,n+1,2):
        if is_prime[i]:
            prime.append(i)

    #print(prime)
    ps=[prime[0]]
    for i in range(1,len(prime)):
        ps.append(ps[-1]+prime[i])

    for i in range(len(prime)-1,-1,-1):
        if ps[i]<n:
            break

        cur=n
        find=True
        for j in range(i,-1,-1):
            if cur-prime[j]<0:
                find=False
                break
            elif cur-prime[j]>0:
                cur-=prime[j]
            else:
                break

        if find:
            ans+=1

print(ans)
