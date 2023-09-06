import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
ans=0
def input():
    x=[]

    for _ in range(n):
        l=[]
        s=sys_input().rstrip()

        for i in range(m):
            if s[i]=='1':
                l.append(1)
            else:
                l.append(0)

        x.append(l)

    return x

a=input()
b=input()

def check():
    for i in range(n):
        for j in range(m):
            if a[i][j]!=b[i][j]:
                return False

    return True


for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if a[x][y]==1:
                        a[x][y]=0
                    else:
                        a[x][y]=1
            ans+=1


if check():
    print(ans)
else:
    print(-1)
