import sys
sys_input=sys.stdin.readline

N=int(sys_input())

arr=[]

for _ in range(N):
    arr.append(int(sys_input()))

if N==0:
    print(0)

else:
    arr.sort()
    cut=round(N*0.15+0.000001)


    ans=round(sum(arr[cut:N-cut])/(N-2*cut)+0.0000001)

    print(ans)
