import sys
sys_input=sys.stdin.readline

n=int(sys_input())
arr=list(map(int,sys_input().rstrip().split()))+[n+1]

checker=-1

for i in range(n-1):
    if arr[i]<arr[i+1]:
        checker=i

if checker==-1:
    print(-1)
    exit()

def find(checker):
    find_idx=n

    for i in range(checker+1,n):
        if arr[checker]<arr[i] and arr[i]<arr[find_idx]:
            find_idx=i

    return find_idx


changer=find(checker)
arr[checker],arr[changer]=arr[changer],arr[checker]

arr[checker+1:]=sorted(arr[checker+1:])

for x in arr[:n]:
    print(x,end=" ")
