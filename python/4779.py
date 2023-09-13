import sys
sys_input=sys.stdin.readline
arr=[]

def dq(idx,n):
    if n==0:
        return

    global arr

    for i in range(idx+(3**(n-1)),idx+2*(3**(n-1))):
        arr[i]=' '

    dq(idx,n-1)
    dq(idx+2*(3**(n-1)),n-1)


while True:
    try:
        n=int(sys_input())
        arr=['-']*((3**n)+1)
        dq(1,n)

        for i in range(1,(3**n)+1):
            print(arr[i],end='')

        print()


    except:
        break
