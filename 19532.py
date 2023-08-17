import sys
sys_input=sys.stdin.readline

a,b,c,d,e,f=map(int,sys_input().rstrip().split())


x=(c*e-b*f)//(a*e-b*d)

if b==0:
    y=(f-d*x)//e
else:
    y=(c-a*x)//b

print(x,y)
