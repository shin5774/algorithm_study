import sys
sys_input=sys.stdin.readline

a=sys_input().rstrip()
b=sys_input().rstrip()
arr=list()

for i in range(len(a)):
    arr.append(int(a[i]))
    arr.append(int(b[i]))


while len(arr)!=2:
    n_arr=[]

    for i in range(len(arr)-1):
        n_arr.append((arr[i]+arr[i+1])%10)

    arr=n_arr

for x in arr:
    print(x,end="")
