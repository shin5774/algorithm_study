import sys
from heapq import heappush,heappop

sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    k=int(sys_input())


    min_q=[]
    max_q=[]
    s=dict()
    cnt=0

    for _ in range(k):
        op,n=sys_input().rstrip().split()
        n=int(n)

        if op=="I":
            heappush(min_q,n)
            heappush(max_q,-n)
            if n in s:
                s[n]+=1
            else:
                s[n]=1

            cnt+=1

        else:
            if n==1:
                while cnt!=0:
                    c=-heappop(max_q)
                    if s[c]!=0:
                        s[c]-=1
                        cnt-=1
                        break
            else:
                while cnt!=0:
                    c=heappop(min_q)
                    if s[c]!=0:
                        s[c]-=1
                        cnt-=1
                        break



    if cnt==0:
        print("EMPTY")
    else:
        while len(min_q)!=0:
            c=heappop(min_q)
            if s[c]!=0:
                heappush(min_q,c)
                break

        while len(max_q)!=0:
            c=-heappop(max_q)
            if s[c]!=0:
                heappush(max_q,-c)
                break

        print(-max_q[0],min_q[0])

for _ in range(T):
    problem()
