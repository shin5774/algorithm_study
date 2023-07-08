import sys,heapq
sys_input=sys.stdin.readline

N=int(sys_input())
dp=[5]*(N+1)
dp[0]=0
dp[1]=1

def find(cur):
    if dp[cur]!=5:
        return dp[cur]

    heap=[]
    for i in range(int(cur**0.5),0,-1):
        heapq.heappush(heap,find(cur-i**2))

    dp[cur]=heapq.heappop(heap)+1

    return dp[cur]

print(find(N))
