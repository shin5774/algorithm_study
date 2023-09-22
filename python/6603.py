import sys
sys_input=sys.stdin.readline

def find(idx):
    global arr,cur

    if len(cur)==6:
        for x in cur:
            print(x,end=" ")
        print()
        return

    if idx==arr[0]+1:
        return

    cur.append(arr[idx])
    find(idx+1)
    cur.pop()
    find(idx+1)

while True:
    arr=list(map(int,sys_input().rstrip().split()))

    if arr[0]==0:
        break

    cur=[]
    find(1)
    print()
