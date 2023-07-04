import sys
sys_input=sys.stdin.readline

N,r,c=map(int,sys_input().rstrip().split())

def dq(i,j,n): #입력좌표와 현재 기준 좌표 비교
    sum=0
    if n==1: #최소단위 2x2인 경우
        if i<r:
            sum=2
        if j<c:
            sum=sum+1
        return sum

    if r>=i+2**(n-1): #4등분의 하단일경우 즉 z의 아래쪽일경우
        sum=sum+2**(2*n-1)
        i=i+2**(n-1) #기준 좌표 갱신
    if c>=j+2**(n-1): #4등분의 우측일경우
        sum=sum+2**(2*(n-1))
        j=j+2**(n-1) #기준 좌표 갱신

    return sum+dq(i,j,n-1)

print(dq(0,0,N))
