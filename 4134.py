import sys
import math
sys_input=sys.stdin.readline

lim=int(4*1e9+1)
T=int(sys_input())

def find_prime(n):
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

for _ in range(T):
    n=int(sys_input())

    if n<=2:
        print(2)
        continue

    while not find_prime(n):
        n+=1

    print(n)
