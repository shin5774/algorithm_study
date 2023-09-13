import sys
sys_input=sys.stdin.readline

n=int(sys_input().rstrip())
work=[]
ans=0

for s in range(1,n+1):
    t,c=map(int,sys_input().rstrip().split())

    if s+t-1>n:
        continue

    work.append((s,s+t-1,c))


def find(idx,e,cost):
    global ans

    if idx==len(work):
        ans=max(ans,cost)
        return

    if work[idx][0]>e:
        find(idx+1,work[idx][1],cost+work[idx][2])

    find(idx+1,e,cost)


find(0,0,0)

print(ans)
