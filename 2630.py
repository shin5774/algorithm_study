import sys
sys_input=sys.stdin.readline

n=int(sys_input())
ans=[0]*2 #white,blue

arr=[list(map(int,sys_input().rstrip().split())) for i in range(n)]

def check(i,j,cn,checker): #해당 구역이 전부 같은 색인지 확인함. True:같은 False:다름
    global arr

    for x in range(i,i+cn):
        for y in range(j,j+cn):
            if checker!=arr[x][y]:
                return False

    return True


def dq(i,j,cn):#divide and conquer 과정
    global arr
    checker=arr[i][j]

    if check(i,j,cn,checker): #구역이 같은색인경우 답 추가과정
        if checker==-0:
            ans[0]=ans[0]+1
        else:
            ans[1]=ans[1]+1
        return

    si=[0,0,cn//2,cn//2]
    sj=[0,cn//2,0,cn//2]

    for s in range(4): #네 구역으로 divide해서 다시 탐색
        ni=i+si[s]
        nj=j+sj[s]

        dq(ni,nj,cn//2)

dq(0,0,n)

for x in ans:
    print(x)
