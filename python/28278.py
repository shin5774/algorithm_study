import sys
sys_input=sys.stdin.readline

arr=[]
n=int(sys_input())
for _ in range(n):

    input=list(map(int,sys_input().rstrip().split()))

    if input[0]==1:
        arr.append(input[1])
    elif input[0]==2:
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
            arr.pop()
    elif input[0]==3:
         print(len(arr))
    elif input[0]==4:
        if len(arr)==0:
            print(1)
        else:
            print(0)
    else:
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
