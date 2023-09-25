import sys
sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())
arr=sys_input().rstrip()
ans=[]

for x in arr:
    while ans and ans[-1]<x and k>0:
        ans.pop()
        k-=1

    ans.append(x)

print(''.join(ans[:len(ans)-k]))
