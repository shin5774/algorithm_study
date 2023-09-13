import sys
sys_input=sys.stdin.readline

TC=int(sys_input())
INF=1e15

def problem():
    N,M,W=map(int,sys_input().rstrip().split())
    edges=[]

    for i in range(M+W):
        s,e,t=map(int,sys_input().rstrip().split())

        if i<M:
            edges.append((e,s,t))
        else:
            t=-t

        edges.append((s,e,t))

    cost=[INF]*(N+1)

    for i in range(N):
        for s,e,t in edges:
            if cost[e]>cost[s]+t: #cost[s]!=INF조건이 없기에 출발지점과 관계없이 음수 사이클을 찾는 로직이 되어버림
                if i==N-1:
                    return True

                cost[e]=cost[s]+t

    return False

for _ in range(TC):
    if problem():
        print("YES")
    else:
        print("NO")
