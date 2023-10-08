import sys
sys_input=sys.stdin.readline

n=int(sys_input())

#n*n에서 확인할수 있는 칸은 2칸,최소한의 경우의수는 n*n//2 이고 나머지칸이 있으면 확인을 한번 더 해야해서 +1
#1은 확인 안해도 알수 있기에 0이 나와야함

if n==1 or n%2==0:
    print(n*n//2)
else:
    print(n*n//2+1)
