import sys

sys_input=sys.stdin.readline
TC=int(sys_input())

def problem():
    N,M,W=map(int,sys_input().rstrip().split())

    graph=[]

    for i in range(M+W):
        s,e,t=map(int,sys_input().rstrip().split())

        if i<M:
            graph.append((e,s,t))
        else:
            t=-t

        graph.append((s,e,t))

    INF=1e15
    cost=[INF]*(N+1)
    cost[1]=0

    for i in range(N):
        for s,e,t in graph:
            if cost[s]+t<cost[e]:
                if i==N-1:
                    return True

                cost[e]=cost[s]+t

    return False

for _ in range(TC):
    if problem():
        print("YES")
    else:
        print("NO")
