import sys
sys_input=sys.stdin.readline

n,k=map(int,sys_input().rstrip().split())
arr=[]
cnt=dict()
multi_tap=set()
ans=0

for x in list(map(int,sys_input().rstrip().split())):
    if x not in cnt:
        cnt[x]=0
    cnt[x]+=1
    arr.append(x)

def find(idx):
    for x in multi_tap:
        if cnt[x]==0:
            multi_tap.remove(x)
            return

    finder=max(multi_tap,key=lambda x:arr[idx+1:].index(x))
    multi_tap.remove(finder)

for idx in range(k):
    cur=arr[idx]

    if cur not in multi_tap:
        if len(multi_tap)==n:
            find(idx)
            ans+=1

        multi_tap.add(cur)

    cnt[cur]-=1

print(ans)
