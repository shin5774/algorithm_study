import sys
sys_input=sys.stdin.readline

n=int(sys_input())
lim=int(sys_input())
d=8 #1,5 배수 2~4 두칸사이의 값
if n==1 or n==5:
    cur_n=n+lim*d

else:
    cur_n=n+(lim//2)*d

    if lim%2!=0:
        cur_n+=-2*n+10

print(cur_n-1)
