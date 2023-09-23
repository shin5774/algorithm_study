import sys
sys_input=sys.stdin.readline
P=10007
n,k=map(int,sys_input().rstrip().split())

def factorial(x):
    cur=1

    for i in range(x,1,-1):
        cur*=i
        cur%=P

    return cur

n_fact=factorial(n)
alpha=(factorial(k)*factorial(n-k))%P
a_pow=P-2
alpha_calc=1

while a_pow>0:

    if a_pow%2==0:
        alpha*=alpha
        alpha%=P
        a_pow//=2
    else:
        alpha_calc*=alpha
        alpha_calc%=P
        a_pow-=1


print((n_fact*alpha_calc)%P)
