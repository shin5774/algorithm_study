import sys
sys_input=sys.stdin.readline

n=int(sys_input())
switch=list(map(int,sys_input().rstrip().split()))

def change(index):
    if switch[index]==1:
        switch[index]=0
        return

    switch[index]=1

def man(index):
    for i in range(index,n+1,index):
       change(i-1)

def girl(index):

    for i in range(n):
        left=index-1-i
        if left<0:
            break

        right=index-1+i
        if right>=n:
            break

        if switch[left]!=switch[right]:
            break

        if left!=right:
            change(left)
        change(right)

    return

t=int(sys_input())

for _ in range(t):
    op,index=map(int,sys_input().rstrip().split())
    if op==1:
        man(index)
    else:
        girl(index)

for i in range(1,n+1):
    if i%20==0:
        print(switch[i-1])
    else:
        print(switch[i-1],end=" ")
