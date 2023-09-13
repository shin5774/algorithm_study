import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[]
virus=deque()
wall=0
ans=0

for i in range(N):
    carr=list(map(int,sys_input().rstrip().split()))
    for j in range(M):
        if carr[j]==2:
            virus.append((i,j))
        elif carr[j]==1:
            wall+=1

    arr.append(carr)


def out_range(i,j):
    if i<0 or j<0 or i>=N or j>=M:
        return True
    return False

def find(s):
    global ans,wall
    q=deque(virus)
    cnt=len(q) #감염영역의 크기

    narr=[a[:] for a in arr]

    for i,j in s:
        narr[i][j]=1

    while len(q)!=0:
        cq=deque(q)
        q=deque()

        while len(cq)!=0:
            i,j=cq.popleft()

            for mi,mj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni=i+mi
                nj=j+mj

                if out_range(ni,nj) or narr[ni][nj]!=0:
                    continue

                q.append((ni,nj))
                narr[ni][nj]=2
                cnt+=1

        if N*M-(wall+3)-cnt<ans: #앞으로 더 가도 ans보다 안커짐
            return

    if N*M-(wall+3)-cnt>ans:
        ans=N*M-(wall+3)-cnt


def selector(r,c,s):
    if len(s)==3:
        find(s)
        return

    for j in range(c+1,M):
        if arr[r][j]!=0:
            continue
        ns=set(s)
        ns.add((r,j))
        selector(r,j,ns)

    for i in range(r+1,N):
        for j in range(0,M):
            if arr[i][j]!=0:
                continue
            ns=set(s)
            ns.add((i,j))
            selector(i,j,ns)

    return


selector(0,-1,set())
print(ans)
