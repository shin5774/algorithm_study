import sys
sys_input=sys.stdin.readline
S=sys_input().rstrip()
alp=ord('a')

arr=[[0]*26 for _ in range(len(S)+1)]

arr[1][ord(S[0])-alp]=1

for i in range(2,len(S)+1):
    arr[i]=arr[i-1][:]
    arr[i][ord(S[i-1])-alp]+=1

T=int(sys_input())

for _ in range(T):
    a,l,r=sys_input().rstrip().split()

    print(arr[int(r)+1][ord(a)-alp]-arr[int(l)][ord(a)-alp])
