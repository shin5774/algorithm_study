import sys
sys_input=sys.stdin.readline

N,r,c=map(int,sys_input().rstrip().split())

def dq(i,j,n): #�Է���ǥ�� ���� ���� ��ǥ ��
    sum=0
    if n==1: #�ּҴ��� 2x2�� ���
        if i<r:
            sum=2
        if j<c:
            sum=sum+1
        return sum

    if r>=i+2**(n-1): #4����� �ϴ��ϰ�� �� z�� �Ʒ����ϰ��
        sum=sum+2**(2*n-1)
        i=i+2**(n-1) #���� ��ǥ ����
    if c>=j+2**(n-1): #4����� �����ϰ��
        sum=sum+2**(2*(n-1))
        j=j+2**(n-1) #���� ��ǥ ����

    return sum+dq(i,j,n-1)

print(dq(0,0,N))
