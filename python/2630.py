import sys
sys_input=sys.stdin.readline

n=int(sys_input())
ans=[0]*2 #white,blue

arr=[list(map(int,sys_input().rstrip().split())) for i in range(n)]

def check(i,j,cn,checker): #�ش� ������ ���� ���� ������ Ȯ����. True:���� False:�ٸ�
    global arr

    for x in range(i,i+cn):
        for y in range(j,j+cn):
            if checker!=arr[x][y]:
                return False

    return True


def dq(i,j,cn):#divide and conquer ����
    global arr
    checker=arr[i][j]

    if check(i,j,cn,checker): #������ �������ΰ�� �� �߰�����
        if checker==-0:
            ans[0]=ans[0]+1
        else:
            ans[1]=ans[1]+1
        return

    si=[0,0,cn//2,cn//2]
    sj=[0,cn//2,0,cn//2]

    for s in range(4): #�� �������� divide�ؼ� �ٽ� Ž��
        ni=i+si[s]
        nj=j+sj[s]

        dq(ni,nj,cn//2)

dq(0,0,n)

for x in ans:
    print(x)
