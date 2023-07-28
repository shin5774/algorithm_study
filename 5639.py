import sys

sys.setrecursionlimit(100000)
sys_input=sys.stdin.readline
arr=[]

x=int(sys_input())

while True:
    try:
        arr.append(x)
        x=int(sys_input())
    except:
        break

tree=[[-1,-1] for _ in range(len(arr))]

def find(n,i):
    idx=0
    while True:
        if n<arr[idx]:
            if tree[idx][0]==-1:
                tree[idx][0]=i
                break
            else:
                idx=tree[idx][0]
        else:
            if tree[idx][1]==-1:
                tree[idx][1]=i
                break
            else:
                idx=tree[idx][1]

for i in range(1,len(arr)):
    find(arr[i],i)

def pre_order(idx):
    if tree[idx][0]!=-1:
        pre_order(tree[idx][0])

    if tree[idx][1]!=-1:
        pre_order(tree[idx][1])

    print(arr[idx])

pre_order(0)
