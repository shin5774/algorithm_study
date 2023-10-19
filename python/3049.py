import sys
sys_input=sys.stdin.readline

n=int(sys_input())

a=n-2 #한 대각선을 만드는 두 점을 제외한 점의 수
ans=0

for i in range(1,a):
    ans+=i*(a-i) #한 점이 만들수 있는 대각선과 해당 대각선의 교차점의 개수

print(ans*n//4) #한 점이 만들수 있는 모든 교차점*모든 점 //중복(교차점을 만드는 점의 개수(4))
