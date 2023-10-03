import sys,math
sys_input=sys.stdin.readline

n,m,k=map(int,sys_input().rstrip().split())
ans=[]

def calc(x,y): #중복이 있는 것들의 경우의수 (n+m)!//(n!*m!)
    return math.factorial(x+y)//(math.factorial(x)*math.factorial(y))


if k>calc(n,m): #전체 경우의수
    print(-1)
    exit()

while k>1:
    front_size=calc(n-1,m) #앞의 a가 들어가는 경우의수
    if k>front_size:  #앞에 a가 들어갈수 없게됨
        k-=front_size
        m-=1
        ans.append('z')
    else:
        n-=1
        ans.append('a')

#남은 것 처리
for _ in range(n):
    ans.append('a')
for _ in range(m):
    ans.append('z')

print(''.join(ans))
