import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[sys_input().rstrip() for _ in range(N)]
mv=[[1,0],[-1,0],[0,1],[0,-1]]
visited=[[0]*M for _ in range(N)]  #0:아직 안지나감 1:지나감(벽 파괴 가능) 2:지나감(파괴불가)
visited[0][0]=1

def out_range(r,c):
    if r<0 or c<0 or r==N or c==M:
        return True
    return False

def bfs():
    ans=-1
    q=deque()
    q.append((0,0,True)) #r,c,벽 부수가 가능 여부
    level=1

    while len(q)!=0:
        cq=deque()

        while len(q)!=0:
            r,c,wall=q.popleft()

            if r==N-1 and c==M-1:
                return level
            
            mv=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

            for p in mv:
                nr=p[0]
                nc=p[1]

                if out_range(nr,nc):
                    continue

                if arr[nr][nc]=='1':
                    if wall and visited[nr][nc]==0:
                        cq.append((nr,nc,False))
                        visited[nr][nc]=2
                        
                else:
                    if visited[nr][nc]==2:
                        if wall:
                            cq.append((nr,nc,wall))
                            visited[nr][nc]=1
                    
                    elif visited[nr][nc]==0:
                        if wall:
                            cq.append((nr,nc,wall))
                            visited[nr][nc]=1
                        else:
                            cq.append((nr,nc,wall))
                            visited[nr][nc]=2

        q=cq.copy()
        cq.clear()
        level+=1

    return ans
            

print(bfs())