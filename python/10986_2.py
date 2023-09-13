import sys,math
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=list(map(int,sys_input().rstrip().split()))
mod_cnt=dict()
ans=0
mod_cnt[arr[0]%m]=1

for i in range(1,n):
    arr[i]+=arr[i-1]
    arr[i]%=m

    if arr[i] not in mod_cnt:
        mod_cnt[arr[i]]=0
    mod_cnt[arr[i]]+=1

if 0 in mod_cnt:
    mod_cnt[0]+=1

for x in mod_cnt:
    ans+=math.comb(mod_cnt[x],2)

print(ans)
