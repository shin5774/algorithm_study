import sys,math
from itertools import combinations
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
arr=list(map(int,sys_input().rstrip().split()))
ans=0
m_cnt=[0]*m

m_cnt[arr[0]%m]+=1

for i in range(1,n):
    arr[i]+=arr[i-1]
    arr[i]%=m
    m_cnt[arr[i]]+=1

ans+=m_cnt[0]+math.comb(m_cnt[0],2)

for i in range(1,m):
    ans+=math.comb(m_cnt[i],2)

print(ans)
