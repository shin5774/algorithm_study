import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline
INF=1e15
N=int(sys_input())
M=int(sys_input())

arr=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,sys_input().rstrip().split())

    arr[a].append((b,c))

begin,end=map(int,sys_input().rstrip().split())

ans=[INF]*(N+1)
ans_root=[[] for _ in range(N+1)]

q=PriorityQueue()
q.put((0,begin,0))

while q.qsize()!=0:
    cost,cur,before=q.get()

    if ans[cur]!=INF:
        continue

    ans[cur]=cost

    ans_root[cur]=ans_root[before].copy()
    ans_root[cur].append(cur)

    for n in arr[cur]:
        next=n[0]
        n_cost=n[1]

        q.put((cost+n_cost,next,cur))

print(ans[end])
print(len(ans_root[end]))
for x in ans_root[end]:
    print(x,end=" ")
