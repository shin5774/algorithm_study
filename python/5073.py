import sys
sys_input=sys.stdin.readline

while True:
    arr=list(map(int,sys_input().rstrip().split()))
    s=set(arr)

    sorted(arr)

    if len(s)==1:
        if arr[0]==0:
            break
        print("Equilateral")

    elif arr[2]>=arr[0]+arr[1]:
        print("Invalid")

    elif len(s)==2:
        print("Isosceles")

    else:
        print("Scalene")
