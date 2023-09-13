import sys
sys_input=sys.stdin.readline

TC=int(sys_input())
INF=1e15

graph=[]
cost=[]

def bellman_ford(start,N):
    for i in range(N):
        for j in range(len(graph)):
            s,e,t=graph[j]
            if cost[s]+t<cost[e]:
                cost[e]=cost[s]+t
                if i==N-1:
                    return True
    return False



def problem():
    N,M,W=map(int,sys_input().rstrip().split())
    global graph,cost
    graph=[]

    for _ in range(M):
        s,e,t=map(int,sys_input().rstrip().split())
        graph.append((s,e,t))
        graph.append((e,s,t))

    for _ in range(W):
        s,e,t=map(int,sys_input().rstrip().split())

        graph.append((s,e,-t))

    cost=[INF]*(N+1)

    if bellman_ford(1,N):
        return True

    return False


for _ in range(TC):
    if problem():
        print("YES")
    else:
        print("NO")
