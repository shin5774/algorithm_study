import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
trees=sorted(list(map(int,sys_input().rstrip().split()))) #정렬까지 시킴

end=trees[-1] #가장 큰값을 끝으로 잡음 or 정렬 안시킬거면 max(trees)해도됨
start=1

while start<=end:
    mid=(start+end)//2
    cur=0
    for t in trees:
        if t>mid:
            cur+=t-mid

    if cur>m:
        start=mid+1
    elif cur<m:
        end=mid-1
    else:
        start=start+1

print(end) #start로 while을 탈출하기에 end가 답이됨
