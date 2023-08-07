import sys
from collections import deque
sys_input=sys.stdin.readline

N,K=map(int,sys_input().rstrip().split())
visited=[False]*(200001)

def find():
    ans=0
    q=deque()
    q.append(N)

    while len(q)!=0:
        cq=deque(q)

        while len(q)!=0:
            x=q.popleft()
            if x==K:
                return ans
            x*=2

            while x<=200000:
                if x==K:
                    return ans

                if visited[x]:
                    break

                cq.append(x)
                visited[x]=True
                x*=2

        while len(cq)!=0:
            x=cq.popleft()

            if x==K:
                return ans

            if x>0 and not visited[x-1]:
                if x-1==K:
                    return ans+1

                q.append(x-1)
                visited[x-1]=True

            if x<200000 and not visited[x+1]:
                if x+1==K:
                    return ans+1

                q.append(x+1)
                visited[x+1]=True

        ans+=1

if N>K:
    print(-(K-N))
else:
    print(find())
