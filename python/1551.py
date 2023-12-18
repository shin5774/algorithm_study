import sys
sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())
arr=list(map(int,sys_input().rstrip().split(',')))

for _ in range(k):
    n_arr=[]

    for i in range(len(arr)-1):
        n_arr.append(arr[i+1]-arr[i])


    arr=n_arr


print(",".join(list(map(str,arr))))
