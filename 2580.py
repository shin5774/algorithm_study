import sys

sys_input=sys.stdin.readline
full_s=set([i for i in range(1,10)])
find=[]
arr=[]

def idx_check(x):
    if x<3:
        return 1
    elif x<6:
        return 2
    else:
        return 3

def dq(idx):
    global arr,find

    if idx==len(find):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")
            print()

        sys.exit()

    x,y=find[idx]
    x_idx=idx_check(x)
    y_idx=idx_check(y)
    s=full_s.copy()


    for i in range(9):
        if arr[x][i] in s:
            s.remove(arr[x][i])

        if arr[i][y] in s:
            s.remove(arr[i][y])

    for i in range(3*(x_idx-1),3*x_idx):
        for j in range(3*(y_idx-1),3*y_idx):
            if arr[i][j] in s:
                s.remove(arr[i][j])

    for n in s:
        arr[x][y]=n
        dq(idx+1)
        arr[x][y]=0


for i in range(9):
    l=list(map(int,sys_input().rstrip().split()))
    for j in range(9):
        if l[j]==0:
            find.append((i,j))
    arr.append(l)

dq(0)
